---
type: Jurisdiction
title: "Hamilton County, IL"
classification: county
fips: "17065"
state: "IL"
demographics:
  population: 7916
  population_under_18: 1731
  population_18_64: 4369
  population_65_plus: 1816
  median_household_income: 65746
  poverty_rate: 12.08
  homeownership_rate: 76.38
  unemployment_rate: 5.13
  median_home_value: 113700
  gini_index: 0.4866
  vacancy_rate: 10.94
  race_white: 7541
  race_black: 17
  race_asian: 41
  race_native: 13
  hispanic: 57
  bachelors_plus: 1665
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/il/districts/senate/58"
    rel: in-district
    area_weight: 0.6238
  - to: "us/states/il/districts/house/116"
    rel: in-district
    area_weight: 0.6238
  - to: "us/states/il/districts/house/117"
    rel: in-district
    area_weight: 0.3762
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Hamilton County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7916 |
| Under 18 | 1731 |
| 18–64 | 4369 |
| 65+ | 1816 |
| Median household income | 65746 |
| Poverty rate | 12.08 |
| Homeownership rate | 76.38 |
| Unemployment rate | 5.13 |
| Median home value | 113700 |
| Gini index | 0.4866 |
| Vacancy rate | 10.94 |
| White | 7541 |
| Black | 17 |
| Asian | 41 |
| Native | 13 |
| Hispanic/Latino | 57 |
| Bachelor's or higher | 1665 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 58](/us/states/il/districts/senate/58.md) — 62% (state senate)
- [IL House District 116](/us/states/il/districts/house/116.md) — 62% (state house)
- [IL House District 117](/us/states/il/districts/house/117.md) — 38% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
