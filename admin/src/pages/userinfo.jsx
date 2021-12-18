import React, { useEffect, useState } from "react";
import { Container, styled } from "@mui/material";
import { useParams } from "react-router-dom";
import axios from "axios";

const CustomContainer = styled(Container)(({ theme }) => ({
  paddingTop: theme.spacing(12),
  height: theme.spacing(75),
}));

export default function Userinfo() {
  const { uid } = useParams();
  const [loadjsx, setLoadJsx] = useState(<></>);

  useEffect(() => {
    axios
      .post("http://localhost:5000/api/admin/user", { id: uid })
      .then((res) => {
        const userData = res.data.user;
        setLoadJsx(
          <div>
            Id: {userData.id}, Username : {userData.username}
          </div>
        );
      })
      .catch((err) => console.log(err));
  }, [uid]);

  return <CustomContainer>{loadjsx}</CustomContainer>;
}
