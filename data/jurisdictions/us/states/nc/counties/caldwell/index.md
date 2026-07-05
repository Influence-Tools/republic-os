---
type: Jurisdiction
title: "Caldwell County, NC"
classification: county
fips: "37027"
state: "NC"
demographics:
  population: 80536
  population_under_18: 15900
  population_18_64: 47364
  population_65_plus: 17272
  median_household_income: 56425
  poverty_rate: 13.37
  homeownership_rate: 73.54
  unemployment_rate: 5.04
  median_home_value: 192200
  gini_index: 0.4353
  vacancy_rate: 11.95
  race_white: 69339
  race_black: 3274
  race_asian: 426
  race_native: 115
  hispanic: 5381
  bachelors_plus: 14648
districts:
  - to: "us/states/nc/districts/05"
    rel: in-district
    area_weight: 0.997
  - to: "us/states/nc/districts/senate/47"
    rel: in-district
    area_weight: 0.726
  - to: "us/states/nc/districts/senate/45"
    rel: in-district
    area_weight: 0.2737
  - to: "us/states/nc/districts/house/87"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Caldwell County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 80536 |
| Under 18 | 15900 |
| 18–64 | 47364 |
| 65+ | 17272 |
| Median household income | 56425 |
| Poverty rate | 13.37 |
| Homeownership rate | 73.54 |
| Unemployment rate | 5.04 |
| Median home value | 192200 |
| Gini index | 0.4353 |
| Vacancy rate | 11.95 |
| White | 69339 |
| Black | 3274 |
| Asian | 426 |
| Native | 115 |
| Hispanic/Latino | 5381 |
| Bachelor's or higher | 14648 |

## Districts

- [NC-05](/us/states/nc/districts/05.md) — 100% (congressional)
- [NC Senate District 47](/us/states/nc/districts/senate/47.md) — 73% (state senate)
- [NC Senate District 45](/us/states/nc/districts/senate/45.md) — 27% (state senate)
- [NC House District 87](/us/states/nc/districts/house/87.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
