"use client";
import Link from "next/link";
import {useEffect, useState} from "react";
export default function Nav(){
  const [logged,setLogged]=useState(false);
  useEffect(()=>setLogged(!!localStorage.getItem("access_token")),[]);
  function logout(){localStorage.removeItem("access_token");window.location.href="/";}
  return <nav className="nav">
    <Link href="/" className="brand">Cyber<span>Guard</span></Link>
    <div className="navLinks">
      <Link href="/training">Training</Link>
      <Link href="/leaderboard">Leaderboard</Link>
      {logged ? <><Link href="/dashboard">Dashboard</Link><button className="linkBtn" onClick={logout}>Logout</button></>
      : <><Link href="/login">Login</Link><Link className="button small" href="/register">Get Started</Link></>}
    </div>
  </nav>
}
