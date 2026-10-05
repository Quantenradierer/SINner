import React, {useState} from "react";
import {Button, FramePentagon, Text} from "@arwes/core";
import {Helmet} from "react-helmet";
import {useNavigate, useParams} from "react-router-dom";
import api from "../../axios";
import i18next from "../../i18n";
import useFloorplan from "../../loader/use_floorplan";
import Warning from "../warning";
import {formFromAttributes, FloorplanTabs, rememberForm} from "./create";
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

export default function FloorplanPage() {
    const {id} = useParams();
    const navigate = useNavigate();
    const {floorplan, status, building, error} = useFloorplan(id);
    const [publishError, setPublishError] = useState(null);
    const [published, setPublished] = useState(false);

    const variation = () => {
        rememberForm(formFromAttributes(floorplan.attributes));
        navigate("/floorplans/create");
    };

    const publish = async () => {
        setPublishError(null);
        try {
            await api.post(`/api/npc_creator/floorplans/${id}/publish/`);
            setPublished(true);
        } catch (e) {
            setPublishError(e.response?.data?.error || i18next.t("prompt_failed_connection"));
        }
    };

    const isUnpublished = floorplan && floorplan.state === "Unpublished" && !published;
    const name = floorplan ? floorplan.attributes.name : "";

    return (
        <div style={{width: "100%", position: "relative"}}>
            <Helmet><title>{`Schattenakte - ${pretty(name)}`}</title></Helmet>
            <FloorplanTabs/>
            {error && <Warning text={i18next.t("floorplan_load_failed")}/>}
            {isUnpublished && <Warning text={i18next.t("floorplan_is_not_published")}/>}
            {!error && !floorplan && <Text>{i18next.t("floorplan_loading")}</Text>}
            {status && (status.state === "queued" || status.state === "rendering") && <Progress status={status}/>}
            {status && status.state === "failed" && (
                <div>
                    <Warning text={status.error || i18next.t("floorplan_failed")}/>
                    <Button FrameComponent={FramePentagon} onClick={variation}>
                        <Text>{i18next.t("floorplan_adjust")}</Text>
                    </Button>
                </div>
            )}
            {floorplan && building && status.state === "done" && (
                <>
                    <div style={{display: "flex", gap: 8, justifyContent: "flex-end", marginBottom: 10}}>
                        <Button FrameComponent={FramePentagon} style={{margin: 0}} onClick={variation}>
                            <Text>{i18next.t("floorplan_variation")}</Text>
                        </Button>
                        {isUnpublished &&
                            <Button FrameComponent={FramePentagon} style={{margin: 0}} onClick={publish}>
                                <Text>{i18next.t("floorplan_publish")}</Text>
                            </Button>}
                    </div>
                    {publishError && <Warning text={publishError}/>}
                    <FloorplanViewer floorplan={floorplan} building={building}/>
                </>
            )}
        </div>
    );
}
