"use client";
import axios from "axios";
import React, { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
const Register: React.FC = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  // const [error, setError] = useState("");
  const [success, setSuccess] = useState(false);

  const handleUsernameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(event.target.value);
  };

  const handleEmailChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPassword(event.target.value);
  };

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setLoading(true);
    // setError(null);
    try {
      const response = await axios.post("http://127.0.0.1:8001/insert/", {
        email: email,
        username: username,
        password: password,
      });
      setLoading(false);
      setSuccess(true);
      console.log("Response from server:", response.data);
      // Optionally, reset the form fields after successful submission
      setUsername("");
      setEmail("");
      setPassword("");
    } catch (error) {
      console.error("Error:", error);
      // setError(error)
      // Handle error here, e.g., display an error message to the user
    }

    // setSuccess(true);
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
        <div className=" max-w-md my-5 mx-auto">
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
            <div className="mb-4">
              <label
                className="block text-gray-700 text-sm font-bold mb-2"
                htmlFor="email"
              >
                Email
              </label>
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="email"
                type="email"
                placeholder="Email"
                value={email}
                onChange={handleEmailChange}
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
                {loading ? "Loading..." : success ? "Success" : "Sign Up"}
              </button>
              {/* {error && (
                <p className="text-red-500 space-x-3 text-xs italic">{error}</p>
              )}  */}
            </div>
          </form>
        </div>
      </CardContent>
    </Card>
  );
};

export default Register;
