import React, {useState} from "react";

import Prompt from "../entity/prompt";
import {useLoaderData} from "react-router";
import CustomComplete from "./complete";
import {Button, FrameBox, FrameCorners, FramePentagon, Text} from "@arwes/core";
import EditableText from "../editable_text";
import AttributeList from "../attribute_list";
import {set} from "animejs";
import i18next from "../../i18n";


const EXAMPLES = []


const CustomPrompt = props => {
    localStorage.setItem('custom_prompt', 'true');

    const default_entity = useLoaderData()

    // get parameters from url
    const url = new URL(window.location.href);
    const search_params = url.searchParams;

    if (default_entity.values['Parameter'] == undefined) {
        default_entity.values['Parameter'] = search_params.get('parameter');
    }
    if (default_entity.values['Aussehen'] == undefined) {
        default_entity.values['Aussehen'] = search_params.get('aussehen');
    }

    const [entity, setEntity] = useState(default_entity);
    const [check, setCheck] = useState(false);
    const [editable, setEditable] = useState(true);

    const modelsOptions = ['--v 1', '--v 2', '--v 3', '--v 4', '--v 5.0', '--v 5.1', '--v 5.2', '--v 6.0', '--niji 4', '--niji 5', '--niji 6']
    const stylizeOptions = ['--s 50', '--s 100', '--s 250', '--s 750']
    const aspectOptions = ['--ar 1:1', '--ar 2:3', '--ar 4:7', '--ar 3:2', '--ar 7:4' ]
    const chaosOptions = ['--chaos 0', '--chaos 7', '--chaos 25', '--chaos 50', '--chaos 100']

    const relevantAttributes = ['Aussehen', 'Parameter']

    function toggleParameterWithOptions(version, options) {
        let parameters = entity.values['Parameter'] || ''
        const onlyRemove = hasParameter(version)

        for (const v of options) {
            parameters = parameters.replace(v, '')
        }

        if (!onlyRemove) {
            parameters = parameters.trim()
            parameters += ' ' + version
        }
        parameters = parameters.trim().replace('  ', ' ')
        entity.values['Parameter'] = parameters
        setEntity(Object.assign({}, entity))
    }

    function hasParameter(toggleParameter) {
        let parameters = entity.values['Parameter'] || ''
        return parameters.includes(toggleParameter)
    }

    function toggleOtherParameter(parameter) {
        let parameters = entity.values['Parameter'] || ''

        if (hasParameter(parameter)) {
            parameters = parameters.replace(parameter, '')
        } else {
            parameters = parameters.trim()
            parameters += ' ' + parameter
        }
        entity.values['Parameter'] = parameters.trim()
        setEntity(Object.assign({}, entity))
    }

    var versionButtons = []
    for (const o of modelsOptions) {
        versionButtons.push(<Button key={o} FrameComponent={FrameCorners} style={{margin: 5, backgroundColor: (entity.values['Parameter'] || '').includes(o)? '#0b8481 ':''}} onClick={() => toggleParameterWithOptions(o, modelsOptions)}>{i18next.t(o)}</Button>)
    }

    var stylizeButtons = []
    for (const o of stylizeOptions) {
        stylizeButtons.push(<Button key={o} FrameComponent={FrameCorners} style={{margin: 5, backgroundColor: (entity.values['Parameter'] || '').includes(o)? '#0b8481 ':''}} onClick={() => toggleParameterWithOptions(o, stylizeOptions)}>{i18next.t(o)}</Button>)
    }

    var aspectRatioButtons = []
    for (const o of aspectOptions) {
        aspectRatioButtons.push(<Button key={o} FrameComponent={FrameCorners} style={{margin: 5, backgroundColor: (entity.values['Parameter'] || '').includes(o)? '#0b8481 ':''}} onClick={() => toggleParameterWithOptions(o, aspectOptions)}>{i18next.t(o)}</Button>)
    }

    var chaosButtons = []
    for (const o of chaosOptions) {
        chaosButtons.push(<Button key={o} FrameComponent={FrameCorners} style={{margin: 5, backgroundColor: (entity.values['Parameter'] || '').includes(o)? '#0b8481 ':''}} onClick={() => toggleParameterWithOptions(o, chaosOptions)}>{i18next.t(o)}</Button>)
    }

    var otherButtons = []
    otherButtons.push(<Button key={'--tile'} FrameComponent={FrameCorners} style={{margin: 5, backgroundColor: (entity.values['Parameter'] || '').includes('--tile')? '#0b8481 ':''}} onClick={() => toggleOtherParameter('--tile')}>{i18next.t('--tile')}</Button>)
    otherButtons.push(<Button key={'--style raw'} FrameComponent={FrameCorners} style={{margin: 5, backgroundColor: (entity.values['Parameter'] || '').includes('--style raw')? '#0b8481 ':''}} onClick={() => toggleOtherParameter('--style raw')}>{i18next.t('--style raw')}</Button>)


    return (
        <Prompt entityType={'custom'} examples={EXAMPLES} entity={entity} setEntity={setEntity}
                setEditable={setEditable}
                check={check} setCheck={setCheck}>

            <FramePentagon style={{width: 950, margin: 15}}>
                <div style={{display: 'flex', width: '100%'}}>

                    <AttributeList listItemWidth={100}
                                   entity={entity}
                                   attributes={relevantAttributes}
                                   approxLineSize={98}
                                   editable={true}
                                   editableDisabled={!editable}
                                   check={check}/>

                </div>
                <div>
                    <hr style={{margin: '2px 0px 0px 2px'}}/>
                    <div style={{display: 'flex', justifyContent: 'center'}}>
                        {versionButtons}
                    </div>
                    <hr style={{margin: '2px 0px 0px 2px'}}/>
                    <div style={{display: 'flex', justifyContent: 'center'}}>
                        {stylizeButtons}
                    </div>
                    <hr style={{margin: '2px 0px 0px 2px'}}/>
                    <div style={{display: 'flex', justifyContent: 'center'}}>
                        {aspectRatioButtons}
                    </div>
                    <hr style={{margin: '2px 0px 0px 2px'}}/>
                    <div style={{display: 'flex', justifyContent: 'center'}}>
                        {chaosButtons}
                    </div>
                    <hr style={{margin: '2px 0px 0px 2px'}}/>
                    <div style={{display: 'flex', justifyContent: 'center'}}>
                        {otherButtons}
                    </div>
                    <hr style={{margin: '2px 0px 0px 2px'}}/>
                    </div>

            </FramePentagon>

        </Prompt>
)
}


export default CustomPrompt;
