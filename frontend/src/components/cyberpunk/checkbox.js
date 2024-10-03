import {useAtom} from "jotai/index";
import {filterAtom} from "../../atom";
import {FrameCorners, Text} from "@arwes/core";
import React from "react";

export const Checkbox = ({children, kind}) => {
    const [filter, setFilter] = useAtom(filterAtom)

    const toggleFilter = () => {
        filter[kind] = !filter[kind]
        setFilter({...filter})
    }

    return <div>
        <div style={{padding: 5, cursor: 'pointer'}} onClick={toggleFilter}>
            <div>
                <FrameCorners cornerWidth={1} cornerLength={4} contentLineWidth={1} palette='primary'
                              style={{width: 16, height: 16, margin: 0, padding: 0}}>
                    {filter[kind] &&
                        <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
                            <line x1="2" y1="2" x2="14" y2="14" stroke="#00F8F8" strokeWidth="2"/>
                            <line x1="2" y1="14" x2="14" y2="2" stroke="#00F8F8" strokeWidth="2"/>
                        </svg>}

                </FrameCorners>
                <Text style={{margin: 5}}>{children}</Text>
            </div>
        </div>
    </div>
}