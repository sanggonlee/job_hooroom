import { POSTING_ATTRIBUTES } from './constants';

export const postingAttributes = Object.freeze([
    POSTING_ATTRIBUTES.isRemote,
    POSTING_ATTRIBUTES.skills,
    POSTING_ATTRIBUTES.location,
    POSTING_ATTRIBUTES.baseLocation,
    POSTING_ATTRIBUTES.employmentType,
    POSTING_ATTRIBUTES.industry,
    POSTING_ATTRIBUTES.jobFunctions,
    POSTING_ATTRIBUTES.seniority,
    POSTING_ATTRIBUTES.words,
]);

export const formatPostingAttributeValue = (attrib) => (bucket = {}) => {
    switch (attrib) {
        case POSTING_ATTRIBUTES.isRemote:
            return bucket.key === 1 ? 'Remote' : 'Onsite';
        default:
            return bucket.key === '' ? 'Unknown' : bucket.key;
    }
};
