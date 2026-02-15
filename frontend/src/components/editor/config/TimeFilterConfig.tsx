import { ParamInput } from './ParamInput';
import { getFieldOptions } from './fieldOptions';

interface TimeFilterConfigProps {
  params: Record<string, any>;
  onChange: (params: Record<string, any>) => void;
}

export function TimeFilterConfig({ params, onChange }: TimeFilterConfigProps) {
  return (
    <div className="space-y-3">
      <ParamInput
        label="Time Reference"
        value={params.server_or_local_time || 'TIME_SERVER'}
        onChange={(v) => onChange({ server_or_local_time: v })}
        options={getFieldOptions('server_or_local_time', params.server_or_local_time || '') ?? undefined}
      />
      <ParamInput
        label="Start Time Mode"
        value={params.time_start_mode || 'TIME_MODE_TEXT'}
        onChange={(v) => onChange({ time_start_mode: v })}
        options={getFieldOptions('time_start_mode', params.time_start_mode || '') ?? undefined}
      />
      <ParamInput
        label="Start Time"
        value={params.time_start || '00:00'}
        onChange={(v) => onChange({ time_start: v })}
        placeholder="HH:MM"
      />
      <ParamInput
        label="End Time Mode"
        value={params.time_end_mode || 'TIME_MODE_TEXT'}
        onChange={(v) => onChange({ time_end_mode: v })}
        options={getFieldOptions('time_end_mode', params.time_end_mode || '') ?? undefined}
      />
      <ParamInput
        label="End Time"
        value={params.time_end || '00:01'}
        onChange={(v) => onChange({ time_end: v })}
        placeholder="HH:MM"
      />
    </div>
  );
}
