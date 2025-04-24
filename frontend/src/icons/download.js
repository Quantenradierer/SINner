import React, {useRef} from 'react';
import {Link, useParams} from 'react-router-dom';
import './circle.css';
import i18n from "../i18n";
import api from "../axios";
import {useEntity} from "../components/entityProvider";
import {Button, FrameBox, FrameHexagon, FrameLines, FrameUnderline, LoadingBars, Text} from "@arwes/core";
import Dialog from "../components/cyberpunk/dialog";
import EncryptedText, {EncryptedTextState} from "../components/cyberpunk/encryptedText";
import {Animator} from "@arwes/animation";
import LoadingBar from "../components/loading_bar";


const download = async (setWaiting, entity, dialogState, setDialogState) => {

  setWaiting(true);
  try {
    const response = await api.get(`/api/npc_creator/entities/${entity.id}/export/`, {params: {fileformat: 'foundryvtt'}})
    if (response.status !== 200) {
      throw new Error('Failed to download file' + response.status);
    }

    const blob = new Blob([response.data]);
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${entity.values.name} - ${entity.values.profession}.json`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    window.URL.revokeObjectURL(url);

    setWaiting(false);
  } catch (error) {
    console.error('Error downloading file:', error);
  }
};


const DownloadState = Object.freeze({
  NOT_STARTED: "not started",
  DOWNLOADING: "downloading",
  DONE: "done"
});


const DownloadDialog = ({dialogState, setDialogState}) => {
  const [downloadWaiting, setDownloadingWaiting] = React.useState(false);
  const [foundryDownload, setFoundryDownload] = React.useState(DownloadState.NOT_STARTED);

  const {entity, _} = useEntity();
  const estimatedTime = 10;

  const encryptMapping = {
    [DownloadState.NOT_STARTED]: EncryptedTextState.STATIC,
    [DownloadState.DOWNLOADING]: EncryptedTextState.RUNNING,
    [DownloadState.DONE]: EncryptedTextState.ENCRYPTING
  }

  return <Dialog dialogState={dialogState} setDialogState={setDialogState} title={i18n.t("entity_download")}>
    <div style={{maxSize: '560px'}}>
      <div>
        <h3>
          <Text>{i18n.t("entity_download_format_picker")}</Text>
        </h3>
      </div>
      <div>
        <div style={{cursor: "pointer"}} onClick={async () => {
          if (!downloadWaiting) {
            setFoundryDownload(DownloadState.DOWNLOADING);
            await download(setDownloadingWaiting, entity, dialogState, setDialogState)
            setFoundryDownload(DownloadState.DONE);
          }
        }}>
          <FrameBox style={{width: '100%'}}>
            <div>
              <Text style={{ fontSize: '20px', fontWeight: 'bold' }}>{i18n.t("entity_download_foundryvtt")}</Text><br/>
              {foundryDownload === DownloadState.DOWNLOADING &&
                  <Animator key={Math.random()} animator={{enter: 300, exit: 300}}><LoadingBar steps={45} estimated_time={12000} title={i18n.t("entity_generate_data")}/></Animator>
              }
              {foundryDownload === DownloadState.DONE &&
              <p key={Math.random()} style={{marginBottom: 0, textAlign: 'left'}}>
                <span state={encryptMapping[foundryDownload]}>- {i18n.t("entity_download_foundryvtt_description1")}</span><br/>
                <span state={encryptMapping[foundryDownload]}>- {i18n.t("entity_download_foundryvtt_description2")}</span><br/>
                <span state={encryptMapping[foundryDownload]}>- {i18n.t("entity_download_foundryvtt_description3")}</span><br/>
                <span state={encryptMapping[foundryDownload]}>- {i18n.t("entity_download_foundryvtt_description4")}</span><br/>
              </p>}
            </div>
          </FrameBox>
        </div>
      </div>
    </div>
  </Dialog>
}


const Download = () => {
  const [dialogState, setDialogState] = React.useState(false);

  return (
      <>
        <DownloadDialog dialogState={dialogState} setDialogState={setDialogState}/>

        <div title={i18n.t("entity_download")} className="hoverresize">
          <svg width="50" height="50" xmlns="http://www.w3.org/2000/svg">
            <Link onClick={() => setDialogState(true)} rel="noopener noreferrer">
              <g className="rotating-circle">
                <circle className="animated-circle" cx="25" cy="25" r="20"></circle>
                <svg x="12" y="12" width="25" height="25" viewBox="0 0 24 24" fill="none"
                     xmlns="http://www.w3.org/2000/svg">
                  <path
                      d="M12 2C11.4477 2 11 2.44772 11 3V13.5858L7.70711 10.2929C7.31658 9.90237 6.68342 9.90237 6.29289 10.2929C5.90237 10.6834 5.90237 11.3166 6.29289 11.7071L12 17.4142L17.7071 11.7071C18.0976 11.3166 18.0976 10.6834 17.7071 10.2929C17.3166 9.90237 16.6834 9.90237 16.2929 10.2929L13 13.5858V3C13 2.44772 12.5523 2 12 2Z"
                      stroke="#00F8F8" fill="#00F8F8"/>
                  <path
                      d="M4 22H20C20.5523 22 21 21.5523 21 21C21 20.4477 20.5523 20 20 20H4C3.44772 20 3 20.4477 3 21C3 21.5523 3.44772 22 4 22Z"
                      stroke="#00F8F8" fill="#00F8F8"/>
                </svg>
              </g>
            </Link>
          </svg>
        </div>
      </>
  );
};


export default Download;