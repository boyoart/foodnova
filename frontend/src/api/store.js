import client from './client';

// Products
export const getProducts = async (categoryId = null) => {
  const params = categoryId ? { category_id: categoryId } : {};
  const response = await client.get('/products', { params });
  return response.data;
};

// Categories
export const getCategories = async () => {
  const response = await client.get('/categories');
  return response.data;
};

// Packs
export const getPacks = async () => {
  const response = await client.get('/packs');
  return response.data;
};

export const getPack = async (packId) => {
  const response = await client.get(`/packs/${packId}`);
  return response.data;
};

// Orders
export const createOrder = async (data) => {
  const response = await client.post('/orders', data);
  return response.data;
};

export const getMyOrders = async () => {
  const response = await client.get('/orders/my');
  return response.data;
};

export const getOrder = async (orderId) => {
  const response = await client.get(`/orders/${orderId}`);
  return response.data;
};

export const uploadReceipt = async (orderId, file) => {
  const formData = new FormData();
  formData.append('file', file);
  const response = await client.post(`/orders/${orderId}/receipt`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return response.data;
};

export const getReceipt = async (orderId) => {
  const response = await client.get(`/orders/${orderId}/receipt`);
  return response.data;
};

// Admin
export const adminGetOrders = async () => {
  const response = await client.get('/admin/orders');
  return response.data;
};

export const adminGetOrder = async (orderId) => {
  const response = await client.get(`/admin/orders/${orderId}`);
  return response.data;
};

export const adminUpdateOrderStatus = async (orderId, status) => {
  const response = await client.patch(`/admin/orders/${orderId}`, { status });
  return response.data;
};

export const adminGetProducts = async () => {
  const response = await client.get('/admin/products');
  return response.data;
};

export const adminCreateProduct = async (data) => {
  const response = await client.post('/admin/products', data);
  return response.data;
};

export const adminUpdateProduct = async (productId, data) => {
  const response = await client.patch(`/admin/products/${productId}`, data);
  return response.data;
};

export const adminDeleteProduct = async (productId) => {
  const response = await client.delete(`/admin/products/${productId}`);
  return response.data;
};

export const adminUpdateReceipt = async (receiptId, data) => {
  const response = await client.patch(`/admin/receipts/${receiptId}`, data);
  return response.data;
};

export const adminUpdatePayment = async (paymentId, data) => {
  const response = await client.patch(`/admin/payments/${paymentId}`, data);
  return response.data;
};

// Admin Categories
export const adminGetCategories = async () => {
  const response = await client.get('/admin/categories');
  return response.data;
};

export const adminCreateCategory = async (name) => {
  const response = await client.post('/admin/categories', { name });
  return response.data;
};

export const adminDeleteCategory = async (categoryId) => {
  const response = await client.delete(`/admin/categories/${categoryId}`);
  return response.data;
};

// Admin Packs
export const adminGetPacks = async () => {
  const response = await client.get('/admin/packs');
  return response.data;
};

export const adminCreatePack = async (data) => {
  const response = await client.post('/admin/packs', data);
  return response.data;
};

export const adminUpdatePack = async (packId, data) => {
  const response = await client.patch(`/admin/packs/${packId}`, data);
  return response.data;
};

export const adminDeletePack = async (packId) => {
  const response = await client.delete(`/admin/packs/${packId}`);
  return response.data;
};

export const adminAddVariant = async (packId, data) => {
  const response = await client.post(`/admin/packs/${packId}/variants`, data);
  return response.data;
};

export const adminUpdateVariant = async (variantId, data) => {
  const response = await client.patch(`/admin/packs/variants/${variantId}`, data);
  return response.data;
};

export const adminDeleteVariant = async (variantId) => {
  const response = await client.delete(`/admin/packs/variants/${variantId}`);
  return response.data;
};

export const adminAddVariantItem = async (variantId, data) => {
  const response = await client.post(`/admin/packs/variants/${variantId}/items`, data);
  return response.data;
};

export const adminDeleteVariantItem = async (itemId) => {
  const response = await client.delete(`/admin/packs/variants/items/${itemId}`);
  return response.data;
};

// Format price helper
export const formatPrice = (amount) => {
  return `₦${amount.toLocaleString()}`;
};
