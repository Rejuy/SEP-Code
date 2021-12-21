import { Check, Close } from "@mui/icons-material";
import {
  styled,
  Container,
  Typography,
  Button,
  Dialog,
  DialogTitle,
  DialogActions,
  DialogContent,
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
  const [open, setOpen] = useState(false);

  const handleDialogClose = () => {
    setOpen(false);
  };

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

  const activateItem = () => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/admin_edit_item", {
        secret_code: localStorage.getItem("secretCode"),
        class: 2,
        item: { ...params.row, activated: 1 },
        delete: false,
      })
      .then((res) => {
        if (res.data.status === 0) {
          params.row.activated = 1;
          params.api.forceUpdate();
        }
      });
  };

  return (
    <>
      <Dialog open={open} onClose={handleDialogClose}>
        <DialogTitle>激活</DialogTitle>
        <DialogContent>
          是否想要激活 "{params.row.name}"?
        </DialogContent>
        <DialogActions>
          <Button
            onClick={() => {
              setOpen(false);
            }}
            variant="outlined"
            color="error"
          >
            否
          </Button>
          <Button
            onClick={() => {
              setOpen(false);
              activateItem();
            }}
            variant="outlined"
            color="success"
          >
            是
          </Button>
        </DialogActions>
      </Dialog>
      <Link to={"/food/" + params.row.id} style={{ marginRight: "10px" }}>
        <Button variant="outlined">修改</Button>
      </Link>
      <Button
        onClick={jsonDetail}
        variant="outlined"
        style={{ marginRight: "10px" }}
      >
        JSON
      </Button>
      {params.row.activated === 1 ? null : (
        <Button
          variant="outlined"
          onClick={(e) => {
            e.stopPropagation();
            setOpen(true);
          }}
          color="success"
        >
          激活
        </Button>
      )}
    </>
  );
}

function Foodpage() {
  const [data, setData] = useState([]);
  const [loaded, setLoaded] = useState(false);
  useEffect(() => {
    axios
      .post(global.config.backendUrl + "/api/v1.0/admin_get_item_list", {
        secret_code: localStorage.getItem("secretCode"),
        offset: 0,
        size: 99999,
        class: 2,
        order: 0,
      })
      .then((res) => {
        setData(res.data.items.sort((a, b) => a.id - b.id));
        setLoaded(true);
      });
  }, []);
  const columns = [
    { field: "id", headerName: "ID", flex: 1 },
    {
      field: "name",
      headerName: "名称",
      headerAlign: "center",
      flex: 4,
    },
    {
      field: "position",
      headerName: "Position",
      headerAlign: "center",
      flex: 1,
    },
    {
      field: "scope",
      headerName: "Scope",
      headerAlign: "center",
      flex: 1,
    },
    {
      field: "type",
      headerName: "类型",
      headerAlign: "center",
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
      field: "activated",
      headerName: "激活",
      headerAlign: "center",
      flex: 1,
      renderCell: (params) => {
        if (params.value === 1) {
          return <Check style={{ width: "100%" }} />;
        } else {
          return <Close style={{ width: "100%" }} />;
        }
      },
    },
    {
      field: "action",
      headerName: "操作",
      headerAlign: "center",
      sortable: false,
      flex: 5,
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
      <Typography variant="h5">加载饮食模块</Typography>
      <CircularProgress />
    </div>
  );

  const dataGridJsx = (
    <div style={{ width: "100%" }}>
      <Typography variant="h5" style={{ marginBottom: "20px" }}>
        饮食
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

export default Foodpage;
