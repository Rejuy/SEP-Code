import {
  styled,
  Container,
  Typography,
  Button,
  CircularProgress,
} from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import axios from "axios";
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "../config";

const CustomContainer = styled(Container)(({ theme }) => ({
  paddingTop: theme.spacing(12),
  height: theme.spacing(75),
  width: "100%",
}));

function ActionInit(params) {
  const jsonDetail = (e) => {
    e.stopPropagation();

    const api = params.api;
    const thisRow = {};

    api
      .getAllColumns()
      .filter((c) => c.field !== "__check__" && !!c)
      .forEach((c) => (thisRow[c.field] = params.getValue(params.id, c.field)));

    return alert(JSON.stringify(thisRow, null, 4));
  };

  return (
    <>
      <Link to={"/comment/" + params.row.id} style={{ marginRight: "10px" }}>
        <Button variant="outlined">修改</Button>
      </Link>
      <Button
        onClick={jsonDetail}
        variant="outlined"
        style={{ marginRight: "10px" }}
      >
        JSON
      </Button>
    </>
  );
}

function Commentpage() {
  const [data, setData] = useState([]);
  const [loaded, setLoaded] = useState(false);
  useEffect(() => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/admin_get_comments", {
        secret_code: localStorage.getItem("secretCode"),
      })
      .then((res) => {
        setData(res.data.comments.sort((a, b) => a.id - b.id));
        setLoaded(true);
      });
  }, []);
  const columns = [
    { field: "id", headerName: "ID", flex: 1 },
    {
      field: "class",
      headerName: "Class",
      headerAlign: "center",
      flex: 1,
    },
    {
      field: "item_id",
      headerName: "Item Id",
      headerAlign: "center",
      flex: 1,
      renderCell: (params) => {
        const id = params.value;
        if (params.row.class === 1) {
          return <Link to={"/course/" + id}>{id}</Link>;
        } else if (params.row.class === 2) {
          return <Link to={"/food/" + id}>{id}</Link>;
        } else if (params.row.class === 3) {
          return <Link to={"/place/" + id}>{id}</Link>;
        } else {
          return <Typography>{id}</Typography>;
        }
      },
    },
    {
      field: "user",
      headerName: "用户名",
      headerAlign: "center",
      align: "center",
      flex: 2,
    },
    {
      field: "user_id",
      headerName: "用户Id",
      headerAlign: "center",
      align: "center",
      flex: 1,
      renderCell: (params) => {
        const id = params.value;
        return <Link to={"/user/" + id}>{id}</Link>;
      },
    },
    {
      field: "star",
      headerName: "评分",
      headerAlign: "center",
      align: "center",
      flex: 1,
    },
    {
      field: "time",
      headerName: "时间",
      headerAlign: "center",
      align: "center",
      flex: 1,
      valueFormatter: (params) => {
        return new Date(params.value).toLocaleDateString("zh-Hans-CN");
      },
    },
    {
      field: "likes",
      headerName: "点赞数",
      headerAlign: "center",
      align: "center",
      flex: 1,
    },
    {
      field: "text",
      headerName: "评论",
      headerAlign: "center",
      flex: 4,
    },
    {
      field: "action",
      headerName: "操作",
      headerAlign: "center",
      sortable: false,
      flex: 4,
      renderCell: ActionInit,
    },
  ];

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
      <Typography variant="h5">加载评论</Typography>
      <CircularProgress />
    </div>
  );

  const dataGridJsx = (
    <div style={{ width: "100%" }}>
      <Typography variant="h5" style={{ marginBottom: "20px" }}>
        评论
      </Typography>
      <DataGrid
        id="datagrid"
        rows={data}
        columns={columns}
        pageSize={8}
        rowsPerPageOptions={[8]}
        checkboxSelection
        autoHeight={true}
        style={{ width: "100%" }}
      />
    </div>
  );

  return (
    <CustomContainer
      style={{ display: "flex", justifyContent: "space-evenly" }}
    >
      {loaded ? dataGridJsx : loadingJsx}
    </CustomContainer>
  );
}

export default Commentpage;
