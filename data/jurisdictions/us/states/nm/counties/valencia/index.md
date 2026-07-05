---
type: Jurisdiction
title: "Valencia County, NM"
classification: county
fips: "35061"
state: "NM"
demographics:
  population: 78458
  population_under_18: 17834
  population_18_64: 45928
  population_65_plus: 14696
  median_household_income: 58933
  poverty_rate: 18.13
  homeownership_rate: 83.18
  unemployment_rate: 6.95
  median_home_value: 223000
  gini_index: 0.4562
  vacancy_rate: 10.32
  race_white: 37987
  race_black: 850
  race_asian: 656
  race_native: 3569
  hispanic: 47732
  bachelors_plus: 15881
districts:
  - to: "us/states/nm/districts/02"
    rel: in-district
    area_weight: 0.6917
  - to: "us/states/nm/districts/01"
    rel: in-district
    area_weight: 0.3083
  - to: "us/states/nm/districts/senate/30"
    rel: in-district
    area_weight: 0.6096
  - to: "us/states/nm/districts/senate/39"
    rel: in-district
    area_weight: 0.2607
  - to: "us/states/nm/districts/senate/29"
    rel: in-district
    area_weight: 0.1297
  - to: "us/states/nm/districts/house/49"
    rel: in-district
    area_weight: 0.6106
  - to: "us/states/nm/districts/house/69"
    rel: in-district
    area_weight: 0.2457
  - to: "us/states/nm/districts/house/7"
    rel: in-district
    area_weight: 0.094
  - to: "us/states/nm/districts/house/8"
    rel: in-district
    area_weight: 0.0496
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Valencia County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 78458 |
| Under 18 | 17834 |
| 18–64 | 45928 |
| 65+ | 14696 |
| Median household income | 58933 |
| Poverty rate | 18.13 |
| Homeownership rate | 83.18 |
| Unemployment rate | 6.95 |
| Median home value | 223000 |
| Gini index | 0.4562 |
| Vacancy rate | 10.32 |
| White | 37987 |
| Black | 850 |
| Asian | 656 |
| Native | 3569 |
| Hispanic/Latino | 47732 |
| Bachelor's or higher | 15881 |

## Districts

- [NM-02](/us/states/nm/districts/02.md) — 69% (congressional)
- [NM-01](/us/states/nm/districts/01.md) — 31% (congressional)
- [NM Senate District 30](/us/states/nm/districts/senate/30.md) — 61% (state senate)
- [NM Senate District 39](/us/states/nm/districts/senate/39.md) — 26% (state senate)
- [NM Senate District 29](/us/states/nm/districts/senate/29.md) — 13% (state senate)
- [NM House District 49](/us/states/nm/districts/house/49.md) — 61% (state house)
- [NM House District 69](/us/states/nm/districts/house/69.md) — 25% (state house)
- [NM House District 7](/us/states/nm/districts/house/7.md) — 9% (state house)
- [NM House District 8](/us/states/nm/districts/house/8.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
