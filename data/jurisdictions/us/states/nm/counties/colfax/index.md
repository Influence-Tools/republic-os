---
type: Jurisdiction
title: "Colfax County, NM"
classification: county
fips: "35007"
state: "NM"
demographics:
  population: 12322
  population_under_18: 2160
  population_18_64: 6613
  population_65_plus: 3549
  median_household_income: 53554
  poverty_rate: 18.15
  homeownership_rate: 71.78
  unemployment_rate: 3.76
  median_home_value: 167200
  gini_index: 0.4608
  vacancy_rate: 44.12
  race_white: 7741
  race_black: 84
  race_asian: 28
  race_native: 338
  hispanic: 5867
  bachelors_plus: 3212
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nm/districts/senate/8"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nm/districts/house/40"
    rel: in-district
    area_weight: 0.8298
  - to: "us/states/nm/districts/house/67"
    rel: in-district
    area_weight: 0.1701
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Colfax County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 12322 |
| Under 18 | 2160 |
| 18–64 | 6613 |
| 65+ | 3549 |
| Median household income | 53554 |
| Poverty rate | 18.15 |
| Homeownership rate | 71.78 |
| Unemployment rate | 3.76 |
| Median home value | 167200 |
| Gini index | 0.4608 |
| Vacancy rate | 44.12 |
| White | 7741 |
| Black | 84 |
| Asian | 28 |
| Native | 338 |
| Hispanic/Latino | 5867 |
| Bachelor's or higher | 3212 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 100% (congressional)
- [NM Senate District 8](/us/states/nm/districts/senate/8.md) — 100% (state senate)
- [NM House District 40](/us/states/nm/districts/house/40.md) — 83% (state house)
- [NM House District 67](/us/states/nm/districts/house/67.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
