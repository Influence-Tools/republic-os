---
type: Jurisdiction
title: "McDonough County, IL"
classification: county
fips: "17109"
state: "IL"
demographics:
  population: 26920
  population_under_18: 4850
  population_18_64: 16871
  population_65_plus: 5199
  median_household_income: 52795
  poverty_rate: 17.2
  homeownership_rate: 63.45
  unemployment_rate: 7.87
  median_home_value: 107500
  gini_index: 0.4662
  vacancy_rate: 12.74
  race_white: 23246
  race_black: 1562
  race_asian: 566
  race_native: 17
  hispanic: 944
  bachelors_plus: 7690
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.8669
  - to: "us/states/il/districts/17"
    rel: in-district
    area_weight: 0.1331
  - to: "us/states/il/districts/senate/47"
    rel: in-district
    area_weight: 0.6893
  - to: "us/states/il/districts/senate/36"
    rel: in-district
    area_weight: 0.3107
  - to: "us/states/il/districts/house/94"
    rel: in-district
    area_weight: 0.6893
  - to: "us/states/il/districts/house/71"
    rel: in-district
    area_weight: 0.3107
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# McDonough County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26920 |
| Under 18 | 4850 |
| 18–64 | 16871 |
| 65+ | 5199 |
| Median household income | 52795 |
| Poverty rate | 17.2 |
| Homeownership rate | 63.45 |
| Unemployment rate | 7.87 |
| Median home value | 107500 |
| Gini index | 0.4662 |
| Vacancy rate | 12.74 |
| White | 23246 |
| Black | 1562 |
| Asian | 566 |
| Native | 17 |
| Hispanic/Latino | 944 |
| Bachelor's or higher | 7690 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 87% (congressional)
- [IL-17](/us/states/il/districts/17.md) — 13% (congressional)
- [IL Senate District 47](/us/states/il/districts/senate/47.md) — 69% (state senate)
- [IL Senate District 36](/us/states/il/districts/senate/36.md) — 31% (state senate)
- [IL House District 94](/us/states/il/districts/house/94.md) — 69% (state house)
- [IL House District 71](/us/states/il/districts/house/71.md) — 31% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
