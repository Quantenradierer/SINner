
const OverlayButtons = (props) => {

    return (
        <div className="no-print" style={{
            zIndex: 1,
            position: 'fixed',
            top: 0,
            left: 0,
            width: '100%',
            height: '90vh',
            pointerEvents: 'none'
        }}>
            <div style={{display: 'flex', justifyContent: 'center', height: '90vh', pointerEvents: 'none'}}>
                <div style={{
                    display: 'flex',
                    maxWidth: 1370 + 24,
                    width: '100%',
                    flexDirection: 'row-reverse',
                    justifyContent: 'flex-start',
                    alignItems: 'flex-end',
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