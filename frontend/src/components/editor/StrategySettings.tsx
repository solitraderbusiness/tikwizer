import { useStrategyStore } from '../../stores/strategyStore';
interface StrategySettingsProps {
  onClose: () => void;
}

export function StrategySettings({ onClose }: StrategySettingsProps) {
  const { name, setName, projectOptions, setProjectOptions } = useStrategyStore();

  const opts = projectOptions;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center" style={{ backgroundColor: 'rgba(0,0,0,0.7)' }}>
      <div
        className="w-[600px] max-h-[80vh] rounded-lg flex flex-col shadow-2xl"
        style={{ backgroundColor: 'var(--color-surface)', border: '1px solid var(--color-border)' }}
      >
        {/* Header */}
        <div
          className="flex items-center justify-between px-4 py-3 border-b rounded-t-lg"
          style={{ borderColor: 'var(--color-border)', backgroundColor: 'var(--color-surface-light)' }}
        >
          <h2 className="text-sm font-semibold" style={{ color: 'var(--color-text)' }}>Strategy Settings</h2>
          <button onClick={onClose} className="text-sm px-2 py-1 rounded border" style={{ borderColor: 'var(--color-border)', color: 'var(--color-text-muted)' }}>
            Close
          </button>
        </div>

        {/* Body */}
        <div className="flex-1 overflow-y-auto p-4 space-y-6">
          {/* Name */}
          <div>
            <label className="block text-xs mb-1 font-medium" style={{ color: 'var(--color-text-muted)' }}>Strategy Name</label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full text-sm px-2 py-1.5 rounded border"
              style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
            />
          </div>

          {/* Magic Number */}
          <div>
            <label className="block text-xs mb-1 font-medium" style={{ color: 'var(--color-text-muted)' }}>Magic Number</label>
            <input
              type="text"
              value={opts.magic_and_other.magic_number}
              onChange={(e) => setProjectOptions({ ...opts, magic_and_other: { ...opts.magic_and_other, magic_number: e.target.value } })}
              className="w-full text-sm px-2 py-1.5 rounded border"
              style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
            />
          </div>

          {/* Version */}
          <div>
            <label className="block text-xs mb-1 font-medium" style={{ color: 'var(--color-text-muted)' }}>Version Number</label>
            <input
              type="text"
              value={opts.description_and_version_number.version_number}
              onChange={(e) => setProjectOptions({ ...opts, description_and_version_number: { ...opts.description_and_version_number, version_number: e.target.value } })}
              className="w-full text-sm px-2 py-1.5 rounded border"
              style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
            />
          </div>

          {/* Description */}
          <div>
            <label className="block text-xs mb-1 font-medium" style={{ color: 'var(--color-text-muted)' }}>Description</label>
            <textarea
              value={opts.description_and_version_number.description}
              onChange={(e) => setProjectOptions({ ...opts, description_and_version_number: { ...opts.description_and_version_number, description: e.target.value } })}
              rows={2}
              className="w-full text-sm px-2 py-1.5 rounded border resize-none"
              style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
            />
          </div>

        </div>
      </div>
    </div>
  );
}
