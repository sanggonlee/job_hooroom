export const POSTING_ATTRIBUTES = Object.freeze({
    isRemote: 'is_remote',
    location: 'location',
    baseLocation: 'base_location',
    employmentType: 'employment_type',
    industry: 'industry',
    jobFunctions: 'job_functions',
    skills: 'skills',
    seniority: 'seniority',
    words: 'words',
});

export const POSTING_ATTRIBUTE_LABELS = Object.freeze({
    [POSTING_ATTRIBUTES.isRemote]: 'Remote',
    [POSTING_ATTRIBUTES.location]: 'Location',
    [POSTING_ATTRIBUTES.baseLocation]: 'Base Location',
    [POSTING_ATTRIBUTES.employmentType]: 'Employment Type',
    [POSTING_ATTRIBUTES.industry]: 'Industry',
    [POSTING_ATTRIBUTES.jobFunctions]: 'Job Functions',
    [POSTING_ATTRIBUTES.skills]: 'Skills',
    [POSTING_ATTRIBUTES.seniority]: 'Seniority',
    [POSTING_ATTRIBUTES.words]: 'Keywords',
});
