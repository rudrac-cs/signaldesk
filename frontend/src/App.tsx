import { useEffect, useState } from 'react'

type Risk = 'low' | 'medium' | 'high'
type Transaction = { id: string; merchant: string; amount: number; currency: string; timestamp: string; risk_score: number; risk_level: Risk; reasons: string[]; status: string }
const API = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'
const formatMoney = (n: number) => new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(n)

export default function App() {
  const [items, setItems] = useState<Transaction[]>([])
  const [selected, setSelected] = useState<string | null>(null)
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(true)
  useEffect(() => {
    fetch(`${API}/api/transactions`)
      .then(r => { if (!r.ok) throw new Error(`API returned ${r.status}`); return r.json() })
      .then((data: Transaction[]) => { setItems(data); setSelected(data[0]?.id ?? null) })
      .catch(() => setError('Could not load transactions. Check that the FastAPI backend is running on port 8000.'))
      .finally(() => setLoading(false))
  }, [])
  const current = items.find(t => t.id === selected)
  return <div className="shell">
    <aside className="sidebar"><div className="brand"><span className="brandicon">S</span> SignalDesk</div><div className="nav active">▦ &nbsp; Review queue</div><div className="nav">◉ &nbsp; Investigation <small>Coming soon</small></div><div className="nav">▤ &nbsp; Reports <small>Coming soon</small></div><div className="sidebarbottom">FinTech UTD · Prototype<br/><span>Synthetic transactions only</span></div></aside>
    <main className="main"><div className="top"><div><div className="eyebrow">FRAUD OPERATIONS / DASHBOARD</div><h1>Transaction review queue</h1><p>Investigate flagged activity with clear, explainable signals.</p></div><div className="demo">DEMO ENVIRONMENT</div></div>
      <div className="stats"><div className="stat"><span>Transactions</span><strong>{items.length}</strong></div><div className="stat"><span>High risk</span><strong>{items.filter(t => t.risk_level === 'high').length}</strong></div><div className="stat"><span>Pending review</span><strong>{items.filter(t => t.status === 'pending_review').length}</strong></div></div>
      <div className="content"><section className="panel"><div className="paneltitle"><h2>Recent activity</h2><span>Sample dataset</span></div>{loading ? <p className="notice">Loading transactions...</p> : error ? <p className="notice error">{error}</p> : items.length === 0 ? <p className="notice">No transactions found.</p> : <div className="tablewrap"><table><thead><tr><th>Transaction</th><th>Merchant</th><th>Amount</th><th>Risk</th></tr></thead><tbody>{items.map(t => <tr key={t.id} onClick={() => setSelected(t.id)} className={t.id === selected ? 'chosen' : ''}><td className="mono">{t.id}</td><td>{t.merchant}</td><td>{formatMoney(t.amount)}</td><td><span className={`pill ${t.risk_level}`}>{t.risk_level}</span></td></tr>)}</tbody></table></div>}</section>
      <section className="panel details"><div className="paneltitle"><h2>Investigation details</h2></div>{current ? <><div className="eyebrow">SELECTED TRANSACTION</div><h3>{current.id}</h3><div className="detailgrid"><div>Merchant<strong>{current.merchant}</strong></div><div>Amount<strong>{formatMoney(current.amount)}</strong></div><div>Risk score<strong>{current.risk_score} / 100</strong></div><div>Risk level<strong><span className={`pill ${current.risk_level}`}>{current.risk_level}</span></strong></div></div><h4>Why it was flagged</h4><ul>{current.reasons.map(reason => <li key={reason}>{reason}</li>)}</ul><div className="note">For reviewer assistance only. Risk flags do not establish fraudulent activity.</div></> : <p className="notice">Choose a transaction to inspect its signals.</p>}</section></div>
    </main>
  </div>
}
