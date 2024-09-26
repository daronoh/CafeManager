import React, { useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { Button, TextField } from '@mui/material';

const CafeForm = ( {initialData, onDataChange, onSubmit} ) => {
    const { register, handleSubmit, watch, formState: { errors } } = useForm({
        defaultValues: initialData || {}
    });

    useEffect(() => {
        const subscription = watch((value) => {
            onDataChange(value); 
        });
        return () => subscription.unsubscribe();
    }, [watch, onDataChange]);

    return (
        <form onSubmit={handleSubmit(onSubmit)} style={{ display: 'flex', flexDirection: 'column', gap: '16px', maxWidth: '400px', margin: 'auto' }}>
            <TextField 
                {...register('name', { 
                    required: 'Name is required', 
                    minLength: { value: 6, message: 'Name must be at least 6 characters' }, 
                    maxLength: { value: 10, message: 'Name cannot exceed 10 characters' } 
                })} 
                label="Name" 
                variant="outlined" 
                fullWidth 
                error={!!errors.name}
                helperText={errors.name?.message}
            />
            
            <TextField 
                {...register('description', { 
                    required: 'Description is required', 
                    maxLength: { value: 256, message: 'Description cannot exceed 256 characters' } 
                })} 
                label="Description" 
                variant="outlined" 
                fullWidth 
                error={!!errors.description}
                helperText={errors.description?.message}
            />
            
            <TextField 
                {...register('location', { 
                    required: 'Location is required', 
                    maxLength: { value: 255, message: 'Location cannot exceed 255 characters' } 
                })} 
                label="Location" 
                variant="outlined" 
                fullWidth 
                error={!!errors.location}
                helperText={errors.location?.message}
            />
            
            <Button type="submit" variant="contained">Submit</Button>
        </form>
    );
};

export default CafeForm;