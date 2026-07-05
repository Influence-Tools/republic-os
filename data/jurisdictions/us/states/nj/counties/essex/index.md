---
type: Jurisdiction
title: "Essex County, NJ"
classification: county
fips: "34013"
state: "NJ"
demographics:
  population: 863002
  population_under_18: 203641
  population_18_64: 536721
  population_65_plus: 122640
  median_household_income: 80789
  poverty_rate: 14.64
  homeownership_rate: 44.9
  unemployment_rate: 8.72
  median_home_value: 524100
  gini_index: 0.5438
  vacancy_rate: 5.1
  race_white: 259184
  race_black: 312703
  race_asian: 52093
  race_native: 4603
  hispanic: 217167
  bachelors_plus: 326308
districts:
  - to: "us/states/nj/districts/11"
    rel: in-district
    area_weight: 0.5868
  - to: "us/states/nj/districts/10"
    rel: in-district
    area_weight: 0.3652
  - to: "us/states/nj/districts/08"
    rel: in-district
    area_weight: 0.0465
  - to: "us/states/nj/districts/senate/27"
    rel: in-district
    area_weight: 0.3552
  - to: "us/states/nj/districts/senate/40"
    rel: in-district
    area_weight: 0.2184
  - to: "us/states/nj/districts/senate/34"
    rel: in-district
    area_weight: 0.1512
  - to: "us/states/nj/districts/senate/29"
    rel: in-district
    area_weight: 0.1496
  - to: "us/states/nj/districts/senate/28"
    rel: in-district
    area_weight: 0.1157
  - to: "us/states/nj/districts/house/27"
    rel: in-district
    area_weight: 0.3552
  - to: "us/states/nj/districts/house/40"
    rel: in-district
    area_weight: 0.2184
  - to: "us/states/nj/districts/house/34"
    rel: in-district
    area_weight: 0.1512
  - to: "us/states/nj/districts/house/29"
    rel: in-district
    area_weight: 0.1496
  - to: "us/states/nj/districts/house/28"
    rel: in-district
    area_weight: 0.1157
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Essex County, NJ

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 863002 |
| Under 18 | 203641 |
| 18–64 | 536721 |
| 65+ | 122640 |
| Median household income | 80789 |
| Poverty rate | 14.64 |
| Homeownership rate | 44.9 |
| Unemployment rate | 8.72 |
| Median home value | 524100 |
| Gini index | 0.5438 |
| Vacancy rate | 5.1 |
| White | 259184 |
| Black | 312703 |
| Asian | 52093 |
| Native | 4603 |
| Hispanic/Latino | 217167 |
| Bachelor's or higher | 326308 |

## Districts

- [NJ-11](/us/states/nj/districts/11.md) — 59% (congressional)
- [NJ-10](/us/states/nj/districts/10.md) — 37% (congressional)
- [NJ-08](/us/states/nj/districts/08.md) — 5% (congressional)
- [NJ Senate District 27](/us/states/nj/districts/senate/27.md) — 36% (state senate)
- [NJ Senate District 40](/us/states/nj/districts/senate/40.md) — 22% (state senate)
- [NJ Senate District 34](/us/states/nj/districts/senate/34.md) — 15% (state senate)
- [NJ Senate District 29](/us/states/nj/districts/senate/29.md) — 15% (state senate)
- [NJ Senate District 28](/us/states/nj/districts/senate/28.md) — 12% (state senate)
- [NJ House District 27](/us/states/nj/districts/house/27.md) — 36% (state house)
- [NJ House District 40](/us/states/nj/districts/house/40.md) — 22% (state house)
- [NJ House District 34](/us/states/nj/districts/house/34.md) — 15% (state house)
- [NJ House District 29](/us/states/nj/districts/house/29.md) — 15% (state house)
- [NJ House District 28](/us/states/nj/districts/house/28.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
