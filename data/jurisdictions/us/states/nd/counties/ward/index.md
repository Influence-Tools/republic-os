---
type: Jurisdiction
title: "Ward County, ND"
classification: county
fips: "38101"
state: "ND"
demographics:
  population: 68973
  population_under_18: 16616
  population_18_64: 42721
  population_65_plus: 9636
  median_household_income: 78238
  poverty_rate: 8.56
  homeownership_rate: 60.78
  unemployment_rate: 3.57
  median_home_value: 267100
  gini_index: 0.4392
  vacancy_rate: 12.06
  race_white: 56047
  race_black: 3271
  race_asian: 1148
  race_native: 1269
  hispanic: 4947
  bachelors_plus: 17247
districts:
  - to: "us/states/nd/districts/00"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nd/districts/senate/4"
    rel: in-district
    area_weight: 0.5408
  - to: "us/states/nd/districts/senate/38"
    rel: in-district
    area_weight: 0.1767
  - to: "us/states/nd/districts/senate/6"
    rel: in-district
    area_weight: 0.125
  - to: "us/states/nd/districts/senate/40"
    rel: in-district
    area_weight: 0.0841
  - to: "us/states/nd/districts/senate/3"
    rel: in-district
    area_weight: 0.0699
  - to: "us/states/nd/districts/house/4b"
    rel: in-district
    area_weight: 0.529
  - to: "us/states/nd/districts/house/38"
    rel: in-district
    area_weight: 0.1767
  - to: "us/states/nd/districts/house/6"
    rel: in-district
    area_weight: 0.125
  - to: "us/states/nd/districts/house/40"
    rel: in-district
    area_weight: 0.0841
  - to: "us/states/nd/districts/house/3"
    rel: in-district
    area_weight: 0.0699
  - to: "us/states/nd/districts/house/4a"
    rel: in-district
    area_weight: 0.0117
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nd]
timestamp: "2026-07-03"
---

# Ward County, ND

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 68973 |
| Under 18 | 16616 |
| 18–64 | 42721 |
| 65+ | 9636 |
| Median household income | 78238 |
| Poverty rate | 8.56 |
| Homeownership rate | 60.78 |
| Unemployment rate | 3.57 |
| Median home value | 267100 |
| Gini index | 0.4392 |
| Vacancy rate | 12.06 |
| White | 56047 |
| Black | 3271 |
| Asian | 1148 |
| Native | 1269 |
| Hispanic/Latino | 4947 |
| Bachelor's or higher | 17247 |

## Districts

- [ND-00](/us/states/nd/districts/00.md) — 100% (congressional)
- [ND Senate District 4](/us/states/nd/districts/senate/4.md) — 54% (state senate)
- [ND Senate District 38](/us/states/nd/districts/senate/38.md) — 18% (state senate)
- [ND Senate District 6](/us/states/nd/districts/senate/6.md) — 12% (state senate)
- [ND Senate District 40](/us/states/nd/districts/senate/40.md) — 8% (state senate)
- [ND Senate District 3](/us/states/nd/districts/senate/3.md) — 7% (state senate)
- [ND House District 4B](/us/states/nd/districts/house/4b.md) — 53% (state house)
- [ND House District 38](/us/states/nd/districts/house/38.md) — 18% (state house)
- [ND House District 6](/us/states/nd/districts/house/6.md) — 12% (state house)
- [ND House District 40](/us/states/nd/districts/house/40.md) — 8% (state house)
- [ND House District 3](/us/states/nd/districts/house/3.md) — 7% (state house)
- [ND House District 4A](/us/states/nd/districts/house/4a.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
