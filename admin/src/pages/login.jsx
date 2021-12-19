import { LockOutlined } from "@mui/icons-material";
import {
  Alert,
  Avatar,
  Box,
  Button,
  Snackbar,
  TextField,
  Typography,
} from "@mui/material";
import axios from "axios";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../config";

export default function Login() {
  const navigate = useNavigate();
  const [username, setusername] = useState("");
  const [password, setpassword] = useState("");
  const [open, setOpen] = useState(false);
  const HandleLogin = () => {
    axios
      .post(global.config.backendUrl + "/api/admin/admin_login", {
        username: username,
        password: password,
      })
      .then((res) => {
        if (res.data.status === 0) {
          global.config.isLogin = true;
          localStorage.setItem("isLogin", true);
          navigate("/");
        } else {
          setOpen(true);
        }
      })
      .catch((err) => console.log(err));
  };
  const HandleClose = () => {
    setOpen(false);
  };

  return (
    <div className="container" style={{ height: "100%", width: "100%" }}>
      <Snackbar open={open} autoHideDuration={6000} onClose={HandleClose}>
        <Alert
          onClose={HandleClose}
          severity="error"
          sx={{
            width: "100%",
            fontSize: "20px",
            display: "flex",
            alignItems: "center",
          }}
        >
          Login Failed, Username password is Admin Admin
        </Alert>
      </Snackbar>
      <Box
        sx={{
          marginTop: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
          <LockOutlined />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign in
        </Typography>
        <Box component="form" noValidate sx={{ mt: 1 }}>
          <TextField
            margin="normal"
            required
            fullWidth
            id="username"
            label="Username"
            name="adminUsername"
            onChange={(e) => {
              setusername(e.target.value);
            }}
            autoFocus
          />
          <TextField
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            onChange={(e) => {
              setpassword(e.target.value);
            }}
            autoComplete="current-password"
          />
          <Button
            type="button"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
            onClick={HandleLogin}
          >
            Sign In
          </Button>
        </Box>
      </Box>
    </div>
  );
}
