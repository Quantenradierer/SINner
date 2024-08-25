
const OverlayButtons = (props) => {

    return (
        <div style={{
            zIndex: 1,
            position: 'fixed',
            top: 0,
            left: 0,
            width: '100%',
            height: '90%',
            pointerEvents: 'none'
        }}>
            <div style={{display: 'flex', justifyContent: 'center', height: '100%', pointerEvents: 'none'}}>
                <div style={{
                    display: 'flex',
                    maxWidth: 1370 + 24,
                    width: '100%',
                    flexDirection: 'row-reverse',
                    justifyContent: 'flex-start',
                    alignItems: 'flex-end',
                    height: '100%',
                    pointerEvents: 'none'
                }}>
                    <div style={{position: 'relative', pointerEvents: 'all'}}>
                        {props.children}
                    </div>
                </div>
            </div>
        </div>
    )
}
export default OverlayButtons;