import React, { useState } from 'react';
import { Button, Dialog, DialogTitle, DialogContent, DialogActions, CircularProgress, Snackbar } from '@mui/material';
import CafeTable from '../components/CafeTable';
import CafeForm from '../components/CafeForm'; 
import { useCafes } from '../hooks/useCafes';

const CafesPage = () => {
    const [open, setOpen] = useState(false);
    const [initialData, setInitialData] = useState(null);
    const { cafesQuery, addCafeMutation, updateCafeMutation, deleteCafeMutation } = useCafes();
    const { data: cafes, isLoading, isError, error } = cafesQuery;
    const [hasUnsavedChanges, setHasUnsavedChanges] = useState(false);

    const handleAddCafe = () => {
        setInitialData(null);
        setOpen(true);
    };

    const handleEditCafe = (cafe) => {
        setInitialData(cafe);
        setOpen(true);
    };

    const handleCancel = () => {
        if (hasUnsavedChanges) {
            if (!window.confirm('You have unsaved changes. Are you sure you want to leave?')) {
                return;
            }
        }
        handleClose();
    };

    const handleClose = () => {
        setOpen(false);
        setInitialData(null);
        setHasUnsavedChanges(false);
    }

    const handleDeleteCafe = (id) => {
        if (window.confirm('Are you sure you want to delete this cafe?')) {
            deleteCafeMutation.mutate(id);
        }
    };

    const handleDataChange = (data) => {
        setHasUnsavedChanges(data !== initialData);
    };

    const onSubmit = async (data) => {
        try {
            if (initialData) {
                await updateCafeMutation.mutateAsync({ cafeId: initialData.id, cafeData: data });
            } else {
                await addCafeMutation.mutateAsync(data);
            }
            handleClose();
        } catch (error) {
            alert(`Error: ${error.response?.data?.detail || 'An error occurred'}`);
        }
    };


    if (isLoading) return <CircularProgress />;
    if (isError) return <Snackbar message={`Error: ${error.message}`} open={true} />;

    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', margin: '20px' }}>
            <Button 
                onClick={handleAddCafe} 
                variant="contained" 
                style={{ marginBottom: '20px', backgroundColor: '#4CAF50', color: 'white', fontWeight: 'bold' }}
            >
                Add New Cafe
            </Button>
            
            <CafeTable cafes={cafes} onEdit={handleEditCafe} onDelete={handleDeleteCafe} />
            
            <Dialog open={open} onClose={handleCancel}>
                <DialogTitle>{initialData ? 'Edit Cafe' : 'Add New Cafe'}</DialogTitle>
                <DialogContent>
                    <CafeForm initialData={initialData} onDataChange={handleDataChange} onSubmit={onSubmit} />
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleCancel} color="primary">Cancel</Button>
                </DialogActions>
            </Dialog>
        </div>
    );
};

export default CafesPage;