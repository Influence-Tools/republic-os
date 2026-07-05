---
type: Jurisdiction
title: "Westchester County, NY"
classification: county
fips: "36119"
state: "NY"
demographics:
  population: 999677
  population_under_18: 212470
  population_18_64: 605678
  population_65_plus: 181529
  median_household_income: 118976
  poverty_rate: 9.01
  homeownership_rate: 61.84
  unemployment_rate: 6.05
  median_home_value: 663200
  gini_index: 0.5383
  vacancy_rate: 5.45
  race_white: 520512
  race_black: 136191
  race_asian: 62523
  race_native: 5261
  hispanic: 273730
  bachelors_plus: 559893
districts:
  - to: "us/states/ny/districts/17"
    rel: in-district
    area_weight: 0.6904
  - to: "us/states/ny/districts/16"
    rel: in-district
    area_weight: 0.2659
  - to: "us/states/ny/districts/senate/40"
    rel: in-district
    area_weight: 0.5235
  - to: "us/states/ny/districts/senate/37"
    rel: in-district
    area_weight: 0.2394
  - to: "us/states/ny/districts/senate/35"
    rel: in-district
    area_weight: 0.1702
  - to: "us/states/ny/districts/senate/34"
    rel: in-district
    area_weight: 0.0116
  - to: "us/states/ny/districts/senate/36"
    rel: in-district
    area_weight: 0.0088
  - to: "us/states/ny/districts/house/93"
    rel: in-district
    area_weight: 0.3802
  - to: "us/states/ny/districts/house/95"
    rel: in-district
    area_weight: 0.185
  - to: "us/states/ny/districts/house/92"
    rel: in-district
    area_weight: 0.1354
  - to: "us/states/ny/districts/house/94"
    rel: in-district
    area_weight: 0.1016
  - to: "us/states/ny/districts/house/88"
    rel: in-district
    area_weight: 0.0572
  - to: "us/states/ny/districts/house/91"
    rel: in-district
    area_weight: 0.0482
  - to: "us/states/ny/districts/house/90"
    rel: in-district
    area_weight: 0.0297
  - to: "us/states/ny/districts/house/89"
    rel: in-district
    area_weight: 0.0162
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ny]
timestamp: "2026-07-03"
---

# Westchester County, NY

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 999677 |
| Under 18 | 212470 |
| 18–64 | 605678 |
| 65+ | 181529 |
| Median household income | 118976 |
| Poverty rate | 9.01 |
| Homeownership rate | 61.84 |
| Unemployment rate | 6.05 |
| Median home value | 663200 |
| Gini index | 0.5383 |
| Vacancy rate | 5.45 |
| White | 520512 |
| Black | 136191 |
| Asian | 62523 |
| Native | 5261 |
| Hispanic/Latino | 273730 |
| Bachelor's or higher | 559893 |

## Districts

- [NY-17](/us/states/ny/districts/17.md) — 69% (congressional)
- [NY-16](/us/states/ny/districts/16.md) — 27% (congressional)
- [NY Senate District 40](/us/states/ny/districts/senate/40.md) — 52% (state senate)
- [NY Senate District 37](/us/states/ny/districts/senate/37.md) — 24% (state senate)
- [NY Senate District 35](/us/states/ny/districts/senate/35.md) — 17% (state senate)
- [NY Senate District 34](/us/states/ny/districts/senate/34.md) — 1% (state senate)
- [NY Senate District 36](/us/states/ny/districts/senate/36.md) — 1% (state senate)
- [NY House District 93](/us/states/ny/districts/house/93.md) — 38% (state house)
- [NY House District 95](/us/states/ny/districts/house/95.md) — 18% (state house)
- [NY House District 92](/us/states/ny/districts/house/92.md) — 14% (state house)
- [NY House District 94](/us/states/ny/districts/house/94.md) — 10% (state house)
- [NY House District 88](/us/states/ny/districts/house/88.md) — 6% (state house)
- [NY House District 91](/us/states/ny/districts/house/91.md) — 5% (state house)
- [NY House District 90](/us/states/ny/districts/house/90.md) — 3% (state house)
- [NY House District 89](/us/states/ny/districts/house/89.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
