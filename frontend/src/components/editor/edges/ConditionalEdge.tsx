import { memo } from 'react';
import { BaseEdge, getStraightPath, type EdgeProps } from '@xyflow/react';

function ConditionalEdgeInner(props: EdgeProps) {
  const { sourceX, sourceY, targetX, targetY, sourceHandleId } = props;
  const isTrue = sourceHandleId === 'blue';

  const [edgePath] = getStraightPath({ sourceX, sourceY, targetX, targetY });

  return (
    <BaseEdge
      {...props}
      path={edgePath}
      style={{
        stroke: isTrue ? '#3b82f6' : '#ef4444',
        strokeWidth: 2,
        strokeDasharray: isTrue ? 'none' : '5,5',
      }}
    />
  );
}

export const ConditionalEdge = memo(ConditionalEdgeInner);
