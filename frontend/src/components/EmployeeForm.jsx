import React, { useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { Button, TextField, RadioGroup, FormControlLabel, Radio, FormControl, InputLabel, MenuItem, Select, FormLabel } from '@mui/material';

const EmployeeForm = ({ onSubmit, initialData, cafes, onDataChange }) => {
    const { register, handleSubmit, watch, setValue, formState: { errors } } = useForm({
        defaultValues: initialData || {}
    });

    useEffect(() => {
        const subscription = watch((value) => {
            onDataChange(value); 
        });
        return () => subscription.unsubscribe();
    }, [watch, onDataChange]);

    const selectedCafeName = watch('cafe_name');
    const selectedGender = watch('gender');

    return (
        <form onSubmit={handleSubmit(onSubmit)} style={{ display: 'flex', flexDirection: 'column', gap: '16px', maxWidth: '400px', margin: 'auto' }}>
            <TextField 
                {...register('name', { required: 'Name is required', minLength: { value: 6, message: 'Minimum length is 6' }, maxLength: { value: 10, message: 'Maximum length is 10' } })} 
                label="Name" 
                variant="outlined" 
                fullWidth
                error={!!errors.name}
                helperText={errors.name?.message}
            />
            
            <TextField 
                {...register('email_address', { required: 'Email address is required' })} 
                label="Email Address" 
                variant="outlined" 
                fullWidth 
                error={!!errors.email_address}
                helperText={errors.email_address?.message}
            />
            
            <TextField 
                {...register('phone_number', {
                    required: 'Phone number is required',
                    validate: {
                        startsWith8or9: value => /^[89]/.test(value) || 'Phone number must start with 8 or 9',
                        isEightDigits: value => /^\d{8}$/.test(value) || 'Phone number must be exactly 8 digits',
                    }
                })} 
                label="Phone Number" 
                variant="outlined" 
                fullWidth 
                error={!!errors.phone_number}
                helperText={errors.phone_number?.message}
            />
            
            <FormControl 
                component="fieldset" 
                {...register('gender')}
                >
                <FormLabel>Gender</FormLabel>
                <RadioGroup 
                    row
                    value={selectedGender || "Male"}
                    onChange={(event) => setValue('gender', event.target.value)}
                    >
                    <FormControlLabel value="Male" control={<Radio />} label="Male" />
                    <FormControlLabel value="Female" control={<Radio />} label="Female" />
                </RadioGroup>
                {errors.gender && <span style={{ color: 'red' }}>{errors.gender.message}</span>}
            </FormControl>

            <FormControl fullWidth variant="outlined">
                <InputLabel id="cafe-select-label">Select Cafe</InputLabel>
                <Select
                    labelId="cafe-select-label"
                    {...register('cafe_name')}
                    value={selectedCafeName || ""}
                    onChange={(event) => setValue('cafe_name', event.target.value)}
                >
                    <MenuItem value="" disabled />
                    {cafes.map(cafe => (
                        <MenuItem key={cafe.name} value={cafe.name}>{cafe.name}</MenuItem>
                    ))}
                </Select>
                {errors.cafe_name && <span style={{ color: 'red' }}>{errors.cafe_name.message}</span>}
            </FormControl>

            <Button type="submit" variant="contained" color="primary" fullWidth>
                Submit
            </Button>
        </form>
    );
};

export default EmployeeForm;