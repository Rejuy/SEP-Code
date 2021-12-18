import React, { useEffect, useState } from "react";
import { CircularProgress, Container, styled, Typography } from "@mui/material";
import { useParams } from "react-router-dom";
import axios from "axios";
import "../config";

const CustomContainer = styled(Container)(({ theme }) => ({
  paddingTop: theme.spacing(12),
  height: theme.spacing(75),
}));

export default function Userinfo() {
  const { uid } = useParams();
  const [userData, setUserData] = useState(null);
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

  const dataJsx = <div>Data</div>;

  useEffect(() => {
    axios
      .post(global.config.backendUrl + "/api/admin/user", { id: uid })
      .then((res) => {
        setUserData(res.data.user);
      })
      .catch((err) => console.log(err));
  }, [uid]);

  return (
    <CustomContainer
      style={{ display: "flex", justifyContent: "space-evenly" }}
    >
      {userData ? dataJsx : loadingJsx}
    </CustomContainer>
  );
}
