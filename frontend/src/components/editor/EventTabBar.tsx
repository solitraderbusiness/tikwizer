import { useEditorStore } from '../../stores/editorStore';
import type { EventName } from '../../types';

const EVENT_TABS: { key: EventName; label: string }[] = [
  { key: 'on_tick', label: 'OnTick' },
  { key: 'on_init', label: 'OnInit' },
  { key: 'on_timer', label: 'OnTimer' },
  { key: 'on_trade', label: 'OnTrade' },
  { key: 'on_chart', label: 'OnChart' },
  { key: 'on_deinit', label: 'OnDeinit' },
];

export function EventTabBar() {
  const activeEvent = useEditorStore((s) => s.activeEvent);
  const setActiveEvent = useEditorStore((s) => s.setActiveEvent);

  return (
    <div className="flex gap-1">
      {EVENT_TABS.map((tab) => (
        <button
          key={tab.key}
          onClick={() => setActiveEvent(tab.key)}
          className="px-3 py-1 text-sm rounded transition-colors"
          style={{
            backgroundColor: activeEvent === tab.key ? 'var(--color-primary)' : 'transparent',
            color: activeEvent === tab.key ? 'white' : 'var(--color-text-muted)',
          }}
        >
          {tab.label}
        </button>
      ))}
    </div>
  );
}
