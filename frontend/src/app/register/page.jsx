"use client";

import Link from "next/link";
import { useState } from "react";
import { api } from "../../lib/api";

export default function Register() {
  const [msg, setMsg] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function submit(e) {
    e.preventDefault();

    setMsg("");
    setError("");
    setLoading(true);

    const form = new FormData(e.currentTarget);

    try {
      await api("/auth/register/", {
        method: "POST",
        body: JSON.stringify({
          username: form.get("username"),
          email: form.get("email"),
          password: form.get("password"),
        }),
      });

      setMsg("Account created successfully. You can now sign in.");
      e.currentTarget.reset();
    } catch (err) {
      setError(err.message || "Unable to create account.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="auth">
      <div className="authCard">

        <div className="brand">
          Cyber<span>Guard</span>
        </div>

        <p className="eyebrow">CREATE ACCOUNT</p>

        <h1>Start learning</h1>

        <p>
          Create your CyberGuard account and begin your cybersecurity
          awareness training.
        </p>

        <form onSubmit={submit}>

          <label>
            Username
            <input
              name="username"
              required
              minLength={3}
              placeholder="Enter username"
            />
          </label>

          <label>
            Email
            <input
              name="email"
              type="email"
              required
              placeholder="you@example.com"
            />
          </label>

          <label>
            Password
            <input
              name="password"
              type="password"
              required
              minLength={8}
              placeholder="Minimum 8 characters"
            />
          </label>

          <button
            className="button full"
            type="submit"
            disabled={loading}
          >
            {loading ? "Creating account..." : "Create Account"}
          </button>

        </form>

        {msg && (
          <p className="success">
            {msg}
          </p>
        )}

        {error && (
          <p className="error">
            {error}
          </p>
        )}

        <p className="authFooter">
          Already registered?{" "}
          <Link href="/login">
            Sign in
          </Link>
        </p>

      </div>
    </main>
  );
}
