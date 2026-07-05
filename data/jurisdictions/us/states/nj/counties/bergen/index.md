---
type: Jurisdiction
title: "Bergen County, NJ"
classification: county
fips: "34003"
state: "NJ"
demographics:
  population: 962316
  population_under_18: 201193
  population_18_64: 586080
  population_65_plus: 175043
  median_household_income: 124884
  poverty_rate: 6.79
  homeownership_rate: 65.34
  unemployment_rate: 5.83
  median_home_value: 623000
  gini_index: 0.4725
  vacancy_rate: 3.92
  race_white: 530150
  race_black: 56128
  race_asian: 162461
  race_native: 2737
  hispanic: 218856
  bachelors_plus: 511552
districts:
  - to: "us/states/nj/districts/05"
    rel: in-district
    area_weight: 0.7348
  - to: "us/states/nj/districts/09"
    rel: in-district
    area_weight: 0.2623
  - to: "us/states/nj/districts/senate/39"
    rel: in-district
    area_weight: 0.4728
  - to: "us/states/nj/districts/senate/38"
    rel: in-district
    area_weight: 0.1715
  - to: "us/states/nj/districts/senate/37"
    rel: in-district
    area_weight: 0.1319
  - to: "us/states/nj/districts/senate/36"
    rel: in-district
    area_weight: 0.1127
  - to: "us/states/nj/districts/senate/40"
    rel: in-district
    area_weight: 0.0908
  - to: "us/states/nj/districts/senate/35"
    rel: in-district
    area_weight: 0.0199
  - to: "us/states/nj/districts/house/39"
    rel: in-district
    area_weight: 0.4728
  - to: "us/states/nj/districts/house/38"
    rel: in-district
    area_weight: 0.1715
  - to: "us/states/nj/districts/house/37"
    rel: in-district
    area_weight: 0.1319
  - to: "us/states/nj/districts/house/36"
    rel: in-district
    area_weight: 0.1127
  - to: "us/states/nj/districts/house/40"
    rel: in-district
    area_weight: 0.0908
  - to: "us/states/nj/districts/house/35"
    rel: in-district
    area_weight: 0.0199
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Bergen County, NJ

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 962316 |
| Under 18 | 201193 |
| 18–64 | 586080 |
| 65+ | 175043 |
| Median household income | 124884 |
| Poverty rate | 6.79 |
| Homeownership rate | 65.34 |
| Unemployment rate | 5.83 |
| Median home value | 623000 |
| Gini index | 0.4725 |
| Vacancy rate | 3.92 |
| White | 530150 |
| Black | 56128 |
| Asian | 162461 |
| Native | 2737 |
| Hispanic/Latino | 218856 |
| Bachelor's or higher | 511552 |

## Districts

- [NJ-05](/us/states/nj/districts/05.md) — 73% (congressional)
- [NJ-09](/us/states/nj/districts/09.md) — 26% (congressional)
- [NJ Senate District 39](/us/states/nj/districts/senate/39.md) — 47% (state senate)
- [NJ Senate District 38](/us/states/nj/districts/senate/38.md) — 17% (state senate)
- [NJ Senate District 37](/us/states/nj/districts/senate/37.md) — 13% (state senate)
- [NJ Senate District 36](/us/states/nj/districts/senate/36.md) — 11% (state senate)
- [NJ Senate District 40](/us/states/nj/districts/senate/40.md) — 9% (state senate)
- [NJ Senate District 35](/us/states/nj/districts/senate/35.md) — 2% (state senate)
- [NJ House District 39](/us/states/nj/districts/house/39.md) — 47% (state house)
- [NJ House District 38](/us/states/nj/districts/house/38.md) — 17% (state house)
- [NJ House District 37](/us/states/nj/districts/house/37.md) — 13% (state house)
- [NJ House District 36](/us/states/nj/districts/house/36.md) — 11% (state house)
- [NJ House District 40](/us/states/nj/districts/house/40.md) — 9% (state house)
- [NJ House District 35](/us/states/nj/districts/house/35.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
