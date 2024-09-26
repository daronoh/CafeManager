import React from 'react';
import { AgGridReact } from 'ag-grid-react';
import { Button } from '@mui/material';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import 'ag-grid-enterprise';
import { Link } from '@tanstack/react-router';


const CafeTable = ({ cafes, onEdit, onDelete }) => {
    const columnDefs = [
        { field: 'name', flex: 2, suppressHeaderMenuButton: true },
        { field: 'description', flex: 4, suppressHeaderMenuButton: true },
        { 
            field: 'employees', 
            flex: 2, 
            suppressHeaderMenuButton: true,
            cellRenderer: (params) => (
                <>
                    <Link
                        to="/employees/$cafeName"
                        params={{
                        cafeName: params.data.name,
                        }}
                    >
                        {params.data.employees}
                    </Link>
                </>
            ),
        },
        { field: 'location', flex: 2, filter: true, suppressHeaderMenuButton: true },
        {
            field: 'actions', flex: 2,
            cellRenderer: (params) => (
                <>
                    <Button onClick={() => onEdit(params.data)}>Edit</Button>
                    <Button onClick={() => onDelete(params.data.id)}>Delete</Button>
                </>
            ),
            suppressHeaderMenuButton: true
        },
    ];

    return (
        <div className="ag-theme-alpine" style={{ height: 800, width: '100%' }}>
            <AgGridReact
                rowData={cafes}
                columnDefs={columnDefs}
                pagination={true}
                paginationPageSize={20}
            />
        </div>
    );
};

export default CafeTable;