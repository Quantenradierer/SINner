import React, { useEffect } from 'react';
import {Button, FrameCorners, FrameLines, FramePentagon, LoadingBars, Text} from "@arwes/core";
import api from "../../axios";


const Logout = props => {

     useEffect(() => {
       (async () => {
         try {
           const {data} = await
                 api.post('/token/logout/',{
                 refresh_token:localStorage.getItem('refresh_token')
                 } ,{headers: {'Content-Type': 'application/json'}},
                 {withCredentials: true});

           localStorage.clear();
           api.defaults.headers.common['Authorization'] = null;
           window.location.href = '/'
           } catch (e) {
             console.log('error on logout', e)
             localStorage.clear();
             window.location.href = '/'
           }
         })();
    }, []);

    return <LoadingBars></LoadingBars>
}

export default Logout;
