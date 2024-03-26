"use client";
import React, { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";

export function ProfileForm() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const handleUsernameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setLoading(true);
    setError(null);
    try {
      // Make API call here, replace 'YOUR_API_ENDPOINT' with your actual endpoint
      const response = await fetch("http://127.0.0.1:8000/login/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username,

          password,
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to register");
      }

      setSuccess(true);
    } catch (error) {
      setError(error.message || "Failed to register");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Card className=" bg-slate-50 ">
      <CardHeader>
        <CardTitle>Register</CardTitle>
        {/* <CardDescription>
          Change your password here. After saving, you'll be logged out.
        </CardDescription> */}
      </CardHeader>
      <CardContent className="space-y-2 ">
        <div className="w-full max-w-md my-5 mx-auto">
          <form
            className="bg-slate-50 shadow-md border-t-primary border-t-4 rounded px-8 pt-6 pb-8 mb-4"
            onSubmit={handleSubmit}
          >
            <div className="mb-4">
              <label
                className="block text-gray-700 text-sm font-bold mb-2"
                htmlFor="username"
              >
                Username
              </label>
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="username"
                type="text"
                placeholder="Username"
                value={username}
                onChange={handleUsernameChange}
                required
              />
            </div>

            <div className="mb-6">
              <label
                className="block text-gray-700 text-sm font-bold mb-2"
                htmlFor="password"
              >
                Password
              </label>
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="password"
                type="password"
                placeholder="Password"
                value={password}
                onChange={handlePasswordChange}
                required
              />
            </div>
            <div className="flex flex-col items-center justify-between space-y-5">
              <button
                className=" bg-blue-500 hover:bg-blue-700  text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                type="submit"
                disabled={loading}
              >
                {" "}
                {loading ? "Loading..." : success ? "Success" : "Log In"}
              </button>
              {error && (
                <p className="text-red-500 space-x-3 text-xs italic">{error}</p>
              )}
            </div>
          </form>
        </div>
      </CardContent>
    </Card>
  );
}
