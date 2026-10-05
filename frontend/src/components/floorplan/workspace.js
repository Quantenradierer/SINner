import React, {useEffect, useState} from "react";
import {Button, FramePentagon, Text} from "@arwes/core";
import {Helmet} from "react-helmet";
import {useNavigate, useParams} from "react-router-dom";
import api from "../../axios";
import i18next from "../../i18n";
import useFloorplan from "../../loader/use_floorplan";
import Warning from "../warning";
import ParamsForm, {FloorplanTabs, formFromAttributes, recallForm, rememberForm, requestFromFormValues} from "./create";
import FloorplanViewer from "./viewer";
import {pretty} from "./overlay";

function Progress({status}) {
    const total = Math.max(status.steps_total, 1);
    const percent = Math.round((100 * status.steps_done) / total);
    return (
        <div style={{margin: "30px 10px"}}>
            <div style={{height: 10, background: "#2f3242"}}>
                <div style={{height: "100%", width: `${percent}%`, background: "#05fdeb", transition: "width .4s"}}/>
            </div>
            <div style={{marginTop: 8, color: "#05fdeb"}}>
                {i18next.t(status.state === "queued" ? "floorplan_queued" : "floorplan_rendering")}
                {status.steps_total > 0 && ` (${status.steps_done}/${status.steps_total})`}
            </div>
        </div>
    );
}

/**
 * One page for creating and viewing: the parameters are in the sidebar, the map beside it.
 * `/floorplans/create` starts empty (with the last used values); `/floorplans/:id` shows that
 * floorplan with its own values in the form, so changing them and generating makes a new one.
 */
export default function FloorplanWorkspace() {
    const {id} = useParams();
    const navigate = useNavigate();
    const {floorplan, status, building, error} = useFloorplan(id);
    const [options, setOptions] = useState(null);
    const [form, setForm] = useState(recallForm);
    const [message, setMessage] = useState(null);
    const [busy, setBusy] = useState(false);
    const [published, setPublished] = useState(false);

    useEffect(() => {
        api.get("/api/npc_creator/floorplans/options/")
            .then((response) => setOptions(response.data))
            .catch(() => setMessage(i18next.t("floorplan_options_failed")));
    }, []);

    // Show the loaded floorplan's own parameters.
    useEffect(() => {
        if (floorplan) setForm(formFromAttributes(floorplan.attributes));
    }, [floorplan && floorplan.id]);

    const set = (name, value) => setForm((f) => {
        const next = {...f, [name]: value};
        if (name === "building_type" && options && !options.rooms[value].includes(next.room)) next.room = "";
        return next;
    });

    const generate = async () => {
        setBusy(true);
        setMessage(null);
        rememberForm(form);
        try {
            const response = await api.post("/api/npc_creator/floorplans/", requestFromFormValues(form));
            setPublished(false);
            navigate(`/floorplans/${response.data.id}`);
        } catch (e) {
            setMessage(e.response?.data?.error || i18next.t("prompt_failed_connection"));
        }
        setBusy(false);
    };

    const publish = async () => {
        setMessage(null);
        try {
            await api.post(`/api/npc_creator/floorplans/${id}/publish/`);
            setPublished(true);
        } catch (e) {
            setMessage(e.response?.data?.error || i18next.t("prompt_failed_connection"));
        }
    };

    const running = status && (status.state === "queued" || status.state === "rendering");
    const isUnpublished = floorplan && floorplan.state === "Unpublished" && !published;
    const canPublish = isUnpublished && status && status.state === "done";
    const title = floorplan ? pretty(floorplan.attributes.name) : i18next.t("tab_header_floorplans_create");

    let placeholder = i18next.t("floorplan_empty");
    if (id && !error && !floorplan) placeholder = i18next.t("floorplan_loading");
    if (running) placeholder = <Progress status={status}/>;
    if (status && status.state === "failed") {
        placeholder = <Warning text={status.error || i18next.t("floorplan_failed")}/>;
    }
    if (error) placeholder = <Warning text={i18next.t("floorplan_load_failed")}/>;

    return (
        <div style={{width: "100%", position: "relative"}}>
            <Helmet><title>{`Schattenakte - ${title}`}</title></Helmet>
            <FloorplanTabs/>
            {isUnpublished && <Warning text={i18next.t("floorplan_is_not_published")}/>}
            {message && <Warning text={message}/>}
            <FloorplanViewer
                floorplan={floorplan}
                building={status && status.state === "done" ? building : null}
                sidebar={options && <ParamsForm options={options} form={form} set={set} onSubmit={generate}
                                                busy={busy || running}/>}
                actions={canPublish && (
                    <div style={{width: 170}}>
                        <Button FrameComponent={FramePentagon} style={{margin: 0}} onClick={publish}>
                            <Text>{i18next.t("floorplan_publish")}</Text>
                        </Button>
                    </div>
                )}
                placeholder={placeholder}/>
        </div>
    );
}
