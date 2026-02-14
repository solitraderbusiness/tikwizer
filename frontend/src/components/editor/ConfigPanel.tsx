import { useEditorStore } from '../../stores/editorStore';
import { BuySellConfig } from './config/BuySellConfig';
import { ConditionConfig } from './config/ConditionConfig';
import { TimeFilterConfig } from './config/TimeFilterConfig';
import { GenericConfig } from './config/GenericConfig';
import type { FlowNodeData } from '../../types';

export function ConfigPanel() {
  const selectedNodeId = useEditorStore((s) => s.selectedNodeId);
  const eventGraphs = useEditorStore((s) => s.eventGraphs);
  const activeEvent = useEditorStore((s) => s.activeEvent);
  const updateNodeData = useEditorStore((s) => s.updateNodeData);
  const removeNode = useEditorStore((s) => s.removeNode);

  if (!selectedNodeId) return null;

  const node = eventGraphs[activeEvent].nodes.find((n) => n.id === selectedNodeId);
  if (!node) return null;

  const data = node.data as FlowNodeData;
  const params = data.params || {};

  const updateParams = (newParams: Record<string, any>) => {
    updateNodeData(selectedNodeId, { params: { ...params, ...newParams } });
  };

  const renderConfig = () => {
    switch (data.block_name_mql) {
      case 'buy_now':
      case 'sell_now':
        return <BuySellConfig params={params} onChange={updateParams} isBuy={data.block_name_mql === 'buy_now'} />;
      case 'condition':
        return <ConditionConfig params={params} onChange={updateParams} />;
      case 'time_filter':
        return <TimeFilterConfig params={params} onChange={updateParams} />;
      default:
        return <GenericConfig params={params} onChange={updateParams} />;
    }
  };

  return (
    <div
      className="w-80 border-l overflow-y-auto flex-shrink-0"
      style={{ backgroundColor: 'var(--color-surface)', borderColor: 'var(--color-border)' }}
    >
      <div className="p-4">
        {/* Node header */}
        <div className="flex items-center justify-between mb-4">
          <div>
            <h2 className="text-sm font-semibold" style={{ color: 'var(--color-text)' }}>{data.blockName}</h2>
            <span className="text-xs" style={{ color: 'var(--color-text-muted)' }}>#{data.id_by_user} · {data.block_name_mql}</span>
          </div>
          <button
            onClick={() => removeNode(selectedNodeId)}
            className="text-xs px-2 py-1 rounded"
            style={{ color: '#ef4444', border: '1px solid #ef4444' }}
          >
            Delete
          </button>
        </div>

        {/* Config form */}
        {renderConfig()}
      </div>
    </div>
  );
}
