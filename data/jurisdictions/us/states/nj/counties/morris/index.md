---
type: Jurisdiction
title: "Morris County, NJ"
classification: county
fips: "34027"
state: "NJ"
demographics:
  population: 514528
  population_under_18: 106211
  population_18_64: 314690
  population_65_plus: 93627
  median_household_income: 137326
  poverty_rate: 4.92
  homeownership_rate: 74.29
  unemployment_rate: 5.2
  median_home_value: 582500
  gini_index: 0.4578
  vacancy_rate: 3.14
  race_white: 351230
  race_black: 16796
  race_asian: 55451
  race_native: 719
  hispanic: 82208
  bachelors_plus: 300104
districts:
  - to: "us/states/nj/districts/11"
    rel: in-district
    area_weight: 0.6419
  - to: "us/states/nj/districts/07"
    rel: in-district
    area_weight: 0.3564
  - to: "us/states/nj/districts/senate/25"
    rel: in-district
    area_weight: 0.4577
  - to: "us/states/nj/districts/senate/24"
    rel: in-district
    area_weight: 0.2694
  - to: "us/states/nj/districts/senate/26"
    rel: in-district
    area_weight: 0.2232
  - to: "us/states/nj/districts/senate/21"
    rel: in-district
    area_weight: 0.0493
  - to: "us/states/nj/districts/house/25"
    rel: in-district
    area_weight: 0.4577
  - to: "us/states/nj/districts/house/24"
    rel: in-district
    area_weight: 0.2694
  - to: "us/states/nj/districts/house/26"
    rel: in-district
    area_weight: 0.2232
  - to: "us/states/nj/districts/house/21"
    rel: in-district
    area_weight: 0.0493
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Morris County, NJ

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 514528 |
| Under 18 | 106211 |
| 18–64 | 314690 |
| 65+ | 93627 |
| Median household income | 137326 |
| Poverty rate | 4.92 |
| Homeownership rate | 74.29 |
| Unemployment rate | 5.2 |
| Median home value | 582500 |
| Gini index | 0.4578 |
| Vacancy rate | 3.14 |
| White | 351230 |
| Black | 16796 |
| Asian | 55451 |
| Native | 719 |
| Hispanic/Latino | 82208 |
| Bachelor's or higher | 300104 |

## Districts

- [NJ-11](/us/states/nj/districts/11.md) — 64% (congressional)
- [NJ-07](/us/states/nj/districts/07.md) — 36% (congressional)
- [NJ Senate District 25](/us/states/nj/districts/senate/25.md) — 46% (state senate)
- [NJ Senate District 24](/us/states/nj/districts/senate/24.md) — 27% (state senate)
- [NJ Senate District 26](/us/states/nj/districts/senate/26.md) — 22% (state senate)
- [NJ Senate District 21](/us/states/nj/districts/senate/21.md) — 5% (state senate)
- [NJ House District 25](/us/states/nj/districts/house/25.md) — 46% (state house)
- [NJ House District 24](/us/states/nj/districts/house/24.md) — 27% (state house)
- [NJ House District 26](/us/states/nj/districts/house/26.md) — 22% (state house)
- [NJ House District 21](/us/states/nj/districts/house/21.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
