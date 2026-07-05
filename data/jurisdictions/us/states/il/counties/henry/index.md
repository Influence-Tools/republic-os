---
type: Jurisdiction
title: "Henry County, IL"
classification: county
fips: "17073"
state: "IL"
demographics:
  population: 48643
  population_under_18: 10516
  population_18_64: 27536
  population_65_plus: 10591
  median_household_income: 71911
  poverty_rate: 8.91
  homeownership_rate: 79.95
  unemployment_rate: 4.83
  median_home_value: 151600
  gini_index: 0.4261
  vacancy_rate: 8.73
  race_white: 42780
  race_black: 535
  race_asian: 254
  race_native: 5
  hispanic: 3366
  bachelors_plus: 11382
districts:
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 0.854
  - to: "us/states/il/districts/17"
    rel: in-district
    area_weight: 0.146
  - to: "us/states/il/districts/senate/47"
    rel: in-district
    area_weight: 0.5775
  - to: "us/states/il/districts/senate/37"
    rel: in-district
    area_weight: 0.2564
  - to: "us/states/il/districts/senate/36"
    rel: in-district
    area_weight: 0.1661
  - to: "us/states/il/districts/house/93"
    rel: in-district
    area_weight: 0.5775
  - to: "us/states/il/districts/house/73"
    rel: in-district
    area_weight: 0.2564
  - to: "us/states/il/districts/house/71"
    rel: in-district
    area_weight: 0.1661
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Henry County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 48643 |
| Under 18 | 10516 |
| 18–64 | 27536 |
| 65+ | 10591 |
| Median household income | 71911 |
| Poverty rate | 8.91 |
| Homeownership rate | 79.95 |
| Unemployment rate | 4.83 |
| Median home value | 151600 |
| Gini index | 0.4261 |
| Vacancy rate | 8.73 |
| White | 42780 |
| Black | 535 |
| Asian | 254 |
| Native | 5 |
| Hispanic/Latino | 3366 |
| Bachelor's or higher | 11382 |

## Districts

- [IL-16](/us/states/il/districts/16.md) — 85% (congressional)
- [IL-17](/us/states/il/districts/17.md) — 15% (congressional)
- [IL Senate District 47](/us/states/il/districts/senate/47.md) — 58% (state senate)
- [IL Senate District 37](/us/states/il/districts/senate/37.md) — 26% (state senate)
- [IL Senate District 36](/us/states/il/districts/senate/36.md) — 17% (state senate)
- [IL House District 93](/us/states/il/districts/house/93.md) — 58% (state house)
- [IL House District 73](/us/states/il/districts/house/73.md) — 26% (state house)
- [IL House District 71](/us/states/il/districts/house/71.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
