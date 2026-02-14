interface TimeFilterConfigProps {
  params: Record<string, any>;
  onChange: (params: Record<string, any>) => void;
}

export function TimeFilterConfig({ params, onChange }: TimeFilterConfigProps) {
  return (
    <div className="space-y-3">
      <div>
        <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>Start Time</label>
        <input
          type="text"
          value={params.timestr_start || '00:00'}
          onChange={(e) => onChange({ timestr_start: e.target.value })}
          placeholder="HH:MM"
          className="w-full text-sm px-2 py-1.5 rounded border"
          style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
        />
      </div>
      <div>
        <label className="block text-xs mb-1" style={{ color: 'var(--color-text-muted)' }}>End Time</label>
        <input
          type="text"
          value={params.timestr_end || '23:59'}
          onChange={(e) => onChange({ timestr_end: e.target.value })}
          placeholder="HH:MM"
          className="w-full text-sm px-2 py-1.5 rounded border"
          style={{ backgroundColor: 'var(--color-surface-light)', borderColor: 'var(--color-border)', color: 'var(--color-text)' }}
        />
      </div>
    </div>
  );
}
