"use client";
import {useEffect,useState} from "react"; import {api} from "../../lib/api";
export default function AdminPanel(){const [data,setData]=useState(null);const [scenarios,setScenarios]=useState([]);const [error,setError]=useState("");
useEffect(()=>{Promise.all([api("/reports/overview/"),api("/scenarios/")]).then(([d,s])=>{setData(d);setScenarios(s.results||s)}).catch(e=>setError(e.message))},[]);
if(error)return <main className="page"><div className="empty">Admin access required or API unavailable: {error}</div></main>;
if(!data)return <main className="page"><div className="empty">Loading admin dashboard...</div></main>;
return <main className="page"><p className="eyebrow">ADMINISTRATION</p><h1>Platform Overview</h1><div className="stats"><div className="stat"><span>Users</span><strong>{data.users}</strong></div><div className="stat"><span>Scenarios</span><strong>{data.scenarios}</strong></div><div className="stat"><span>Attempts</span><strong>{data.attempts}</strong></div><div className="stat"><span>Points Awarded</span><strong>{data.total_points_awarded}</strong></div></div><div className="panel adminList"><h2>Scenario Library</h2>{scenarios.map(s=><div className="activity" key={s.id}><span>🛡️</span><div><b>{s.title}</b><small>{s.category} • {s.difficulty} • {s.points} points</small></div></div>)}</div></main>}
