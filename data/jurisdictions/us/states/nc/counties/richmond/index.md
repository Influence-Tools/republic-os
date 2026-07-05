---
type: Jurisdiction
title: "Richmond County, NC"
classification: county
fips: "37153"
state: "NC"
demographics:
  population: 42344
  population_under_18: 9943
  population_18_64: 24731
  population_65_plus: 7670
  median_household_income: 44883
  poverty_rate: 25.22
  homeownership_rate: 65.95
  unemployment_rate: 9.79
  median_home_value: 127800
  gini_index: 0.4752
  vacancy_rate: 14.41
  race_white: 23733
  race_black: 13279
  race_asian: 418
  race_native: 846
  hispanic: 3297
  bachelors_plus: 6275
districts:
  - to: "us/states/nc/districts/08"
    rel: in-district
    area_weight: 0.998
  - to: "us/states/nc/districts/senate/29"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/nc/districts/house/52"
    rel: in-district
    area_weight: 0.9995
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Richmond County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 42344 |
| Under 18 | 9943 |
| 18–64 | 24731 |
| 65+ | 7670 |
| Median household income | 44883 |
| Poverty rate | 25.22 |
| Homeownership rate | 65.95 |
| Unemployment rate | 9.79 |
| Median home value | 127800 |
| Gini index | 0.4752 |
| Vacancy rate | 14.41 |
| White | 23733 |
| Black | 13279 |
| Asian | 418 |
| Native | 846 |
| Hispanic/Latino | 3297 |
| Bachelor's or higher | 6275 |

## Districts

- [NC-08](/us/states/nc/districts/08.md) — 100% (congressional)
- [NC Senate District 29](/us/states/nc/districts/senate/29.md) — 100% (state senate)
- [NC House District 52](/us/states/nc/districts/house/52.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
