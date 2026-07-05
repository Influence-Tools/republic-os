---
type: Jurisdiction
title: "Garfield County, OK"
classification: county
fips: "40047"
state: "OK"
demographics:
  population: 62146
  population_under_18: 16105
  population_18_64: 35635
  population_65_plus: 10406
  median_household_income: 66182
  poverty_rate: 12.55
  homeownership_rate: 65.97
  unemployment_rate: 4.87
  median_home_value: 160100
  gini_index: 0.4312
  vacancy_rate: 14.07
  race_white: 45476
  race_black: 1486
  race_asian: 798
  race_native: 1213
  hispanic: 9451
  bachelors_plus: 12219
districts:
  - to: "us/states/ok/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/senate/19"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ok/districts/house/38"
    rel: in-district
    area_weight: 0.5503
  - to: "us/states/ok/districts/house/59"
    rel: in-district
    area_weight: 0.2713
  - to: "us/states/ok/districts/house/58"
    rel: in-district
    area_weight: 0.1614
  - to: "us/states/ok/districts/house/40"
    rel: in-district
    area_weight: 0.0169
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Garfield County, OK

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 62146 |
| Under 18 | 16105 |
| 18–64 | 35635 |
| 65+ | 10406 |
| Median household income | 66182 |
| Poverty rate | 12.55 |
| Homeownership rate | 65.97 |
| Unemployment rate | 4.87 |
| Median home value | 160100 |
| Gini index | 0.4312 |
| Vacancy rate | 14.07 |
| White | 45476 |
| Black | 1486 |
| Asian | 798 |
| Native | 1213 |
| Hispanic/Latino | 9451 |
| Bachelor's or higher | 12219 |

## Districts

- [OK-03](/us/states/ok/districts/03.md) — 100% (congressional)
- [OK Senate District 19](/us/states/ok/districts/senate/19.md) — 100% (state senate)
- [OK House District 38](/us/states/ok/districts/house/38.md) — 55% (state house)
- [OK House District 59](/us/states/ok/districts/house/59.md) — 27% (state house)
- [OK House District 58](/us/states/ok/districts/house/58.md) — 16% (state house)
- [OK House District 40](/us/states/ok/districts/house/40.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
