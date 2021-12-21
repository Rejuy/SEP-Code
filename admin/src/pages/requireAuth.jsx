import React from "react";
import { Navigate } from "react-router-dom";
import "../config";

export default function RequireAuth({ children }) {
  if (
    !localStorage.getItem("secretCode") ||
    localStorage.getItem("secretCode") === ""
  ) {
    return <Navigate to="/login" />;
  }
  return children;
}
