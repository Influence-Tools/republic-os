---
type: Jurisdiction
title: "Rowan County, NC"
classification: county
fips: "37159"
state: "NC"
demographics:
  population: 149875
  population_under_18: 33228
  population_18_64: 90054
  population_65_plus: 26593
  median_household_income: 65725
  poverty_rate: 15.99
  homeownership_rate: 72.32
  unemployment_rate: 5.32
  median_home_value: 238400
  gini_index: 0.4448
  vacancy_rate: 9.35
  race_white: 104854
  race_black: 23658
  race_asian: 1200
  race_native: 798
  hispanic: 17788
  bachelors_plus: 31708
districts:
  - to: "us/states/nc/districts/06"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/senate/33"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/nc/districts/house/76"
    rel: in-district
    area_weight: 0.5
  - to: "us/states/nc/districts/house/77"
    rel: in-district
    area_weight: 0.2661
  - to: "us/states/nc/districts/house/83"
    rel: in-district
    area_weight: 0.2337
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Rowan County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 149875 |
| Under 18 | 33228 |
| 18–64 | 90054 |
| 65+ | 26593 |
| Median household income | 65725 |
| Poverty rate | 15.99 |
| Homeownership rate | 72.32 |
| Unemployment rate | 5.32 |
| Median home value | 238400 |
| Gini index | 0.4448 |
| Vacancy rate | 9.35 |
| White | 104854 |
| Black | 23658 |
| Asian | 1200 |
| Native | 798 |
| Hispanic/Latino | 17788 |
| Bachelor's or higher | 31708 |

## Districts

- [NC-06](/us/states/nc/districts/06.md) — 100% (congressional)
- [NC Senate District 33](/us/states/nc/districts/senate/33.md) — 100% (state senate)
- [NC House District 76](/us/states/nc/districts/house/76.md) — 50% (state house)
- [NC House District 77](/us/states/nc/districts/house/77.md) — 27% (state house)
- [NC House District 83](/us/states/nc/districts/house/83.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
