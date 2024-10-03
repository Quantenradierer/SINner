import {useEntity} from "../components/entityProvider";
import React, {useState} from "react";
import is_logged_in from "../is_loggin_in";
import i18n from "../i18n";
import {Link} from "react-router-dom";

export const ProfileButton = () => {
    return (
        <Link to='/profile'>
        <div title={i18n.t("header_profile")}>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="40"
                height="40"
                viewBox="0 0 24 24"
                fill="none"
                stroke="#000"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
            >
                <circle cx="12" cy="12" r="10" stroke="#00F8F8" strokeWidth="2"/>
                <circle cx="12" cy="10" r="3" stroke="#00F8F8"/>
                <path d="M6 20c0-4 4-6 6-6s6 2 6 6" stroke="#00F8F8" strokeWidth="2" fill="none"/>
            </svg>
        </div>
        </Link>
    );
}