import { styled, Container, Typography } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import axios from "axios";
import React, { useEffect, useState } from "react";

const CustomContainer = styled(Container)(({ theme }) => ({
  paddingTop: theme.spacing(12),
  height: theme.spacing(75),
}));

function Coursepage() {
  const [data, setData] = useState([]);
  useEffect(() => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/admin_get_item_list", {
        secret_code: localStorage.getItem("secretCode"),
        class: 3,
        order: 0,
        offset: 0,
        size: 1000,
      })
      .then((res) => {
        console.log(res);
        setData(res.data.items);
      });
  }, []);
  const columns = [
    { field: "id", headerName: "ID", width: 70 },
    {
      field: "name",
      headerName: "Course Name",
      headerAlign: "center",
      width: 200,
    },
  ];
  return (
    <CustomContainer>
      <Typography variant="h5" style={{ marginBottom: "20px" }}>
        Courses
      </Typography>
      <DataGrid
        rows={data}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5]}
        checkboxSelection
      />
    </CustomContainer>
  );
}

export default Coursepage;
