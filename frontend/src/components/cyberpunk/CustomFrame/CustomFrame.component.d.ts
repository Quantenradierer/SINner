import { ReactElement } from 'react';
import { WithAnimatorInputProps } from '@arwes/animation';
import { FrameProps } from '@arwes/core/lib/utils/Frame';
interface CustomFrame<E> extends FrameProps<E> {
    lineWidth?: number;
    squareSize?: number;
}
declare function FramePentagon<E>(props: CustomFrame<E> & WithAnimatorInputProps): ReactElement;
declare namespace FramePentagon {
    var defaultProps: {
        lineWidth: number;
        squareSize: number;
    };
}
export { CustomFrame, FramePentagon };
