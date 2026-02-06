import apiClient from '../lib/api';

export interface Article {
    id: number;
    title: string;
    slug: string;
    excerpt: string;
    content: string | null;
    image: string;
    author_name: string;
    author_avatar: string;
    date: string;
    read_time: string;
    color_class: string;
    created_at: string;
}

const articlesService = {
    async getAll(skip: number = 0, limit: number = 100): Promise<Article[]> {
        const response = await apiClient.get<Article[]>('/api/articles', {
            params: { skip, limit },
        });
        return response.data;
    },

    async getBySlug(slug: string): Promise<Article> {
        const response = await apiClient.get<Article>(`/api/articles/${slug}`);
        return response.data;
    },

    async create(data: Partial<Article>): Promise<Article> {
        const response = await apiClient.post<Article>('/api/articles', data);
        return response.data;
    },

    async update(id: number, data: Partial<Article>): Promise<Article> {
        const response = await apiClient.put<Article>(`/api/articles/${id}`, data);
        return response.data;
    },

    async delete(id: number): Promise<void> {
        await apiClient.delete(`/api/articles/${id}`);
    },
};

export default articlesService;
