import React, { useEffect, useState } from "react";
import {
  Button,
  Checkbox,
  CircularProgress,
  Container,
  FormControlLabel,
  FormGroup,
  styled,
  TextField,
  Typography,
} from "@mui/material";
import { useNavigate, useParams } from "react-router-dom";
import axios from "axios";
import "../config";
import { Box } from "@mui/system";
import { AccountBox } from "@mui/icons-material";

const CustomContainer = styled(Container)(({ theme }) => ({
  paddingTop: theme.spacing(12),
  height: theme.spacing(75),
}));

export default function Userinfo() {
  const navigate = useNavigate();
  const { uid } = useParams();
  const [userData, setUserData] = useState({
    id: -1,
    user_name: "",
    email: "",
    user_icon: "",
    activated: false,
    account_birth: new Date(),
    collection_count: 0,
    like_count: 0,
    comment_count: 0,
    item_count: 0,
  });
  const [dataJsx, setDataJsx] = useState(<></>);
  const loadingJsx = (
    <div
      className="loading"
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "space-evenly",
      }}
    >
      <Typography variant="h5">Loading User</Typography>
      <CircularProgress />
    </div>
  );

  useEffect(() => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/user", {
        secret_code: localStorage.getItem("secretCode"),
        id: uid,
      })
      .then((res) => {
        setUserData(res.data.user);
      })
      .catch((err) => console.log(err));
  }, [uid]);

  useEffect(() => {
    var user_icon_element,
      user_icon_url = userData.user_icon;
    if (user_icon_url) {
      user_icon_element = (
        <img
          src={user_icon_url}
          alt="User Icon"
          style={{
            width: "64px",
            height: "64px",
            borderRadius: "2px",
            objectFit: "fill",
          }}
        />
      );
    } else {
      user_icon_element = (
        <AccountBox
          style={{
            width: "64px",
            height: "64px",
          }}
        />
      );
    }
    setDataJsx(
      <Box
        sx={{
          "& .MuiTextField-root": { m: 1, width: "25ch" },
        }}
        noValidate
        autoComplete="off"
      >
        <div style={{ display: "flex", justifyContent: "space-between" }}>
          {user_icon_element}
          <TextField
            label="User Icon"
            variant="standard"
            value={userData.user_icon || ""}
            onChange={(e) => {
              if (e.target.value !== "") {
                setUserData((prev) => ({ ...prev, user_icon: e.target.value }));
              } else {
                setUserData((prev) => ({ ...prev, user_icon: null }));
              }
            }}
          />
        </div>
        <div>
          <TextField
            InputProps={{
              readOnly: true,
            }}
            label="User Id"
            variant="standard"
            value={userData.id}
          />
          <TextField
            required
            label="Username"
            variant="standard"
            value={userData.user_name}
            onChange={(e) => {
              setUserData((prev) => ({ ...prev, user_name: e.target.value }));
            }}
          />
        </div>
        <div style={{ display: "flex", alignItems: "center" }}>
          <TextField
            required
            label="Email"
            variant="standard"
            value={userData.email}
            onChange={(e) => {
              setUserData((prev) => ({ ...prev, email: e.target.value }));
            }}
          />
          <FormGroup>
            <FormControlLabel
              control={
                <Checkbox
                  checked={userData.activated}
                  onChange={(e) => {
                    setUserData((prev) => ({
                      ...prev,
                      activated: e.target.checked,
                    }));
                  }}
                />
              }
              label="Activated"
            />
          </FormGroup>
        </div>
        <div>
          <Button
            variant="outlined"
            color="success"
            fullWidth
            onClick={() => {
              axios
                .post(global.config.backendUrl + "/api/v1.0/edit_user", {
                  secret_code: localStorage.getItem("secretCode"),
                  user: userData,
                })
                .then((res) => {
                  navigate("/users");
                });
            }}
          >
            Change
          </Button>
        </div>
        <div style={{ marginTop: "10px" }}>
          <Button
            variant="outlined"
            color="error"
            fullWidth
            onClick={() => {
              axios
                .post(global.config.backendUrl + "/api/v1.0/delete_user", {
                  secret_code: localStorage.getItem("secretCode"),
                  id: userData.id,
                })
                .then((res) => {
                  navigate("/users");
                });
            }}
          >
            Delete
          </Button>
        </div>
        <div style={{ marginTop: "10px" }}>
          <Button
            variant="outlined"
            color="primary"
            fullWidth
            onClick={() => {
              navigate("/users");
            }}
          >
            Back
          </Button>
        </div>
      </Box>
    );
  }, [userData, navigate]);

  return (
    <CustomContainer
      style={{ display: "flex", justifyContent: "space-evenly" }}
    >
      {userData ? dataJsx : loadingJsx}
    </CustomContainer>
  );
}
