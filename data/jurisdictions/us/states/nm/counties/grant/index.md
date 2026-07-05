---
type: Jurisdiction
title: "Grant County, NM"
classification: county
fips: "35017"
state: "NM"
demographics:
  population: 27775
  population_under_18: 4974
  population_18_64: 14382
  population_65_plus: 8419
  median_household_income: 44958
  poverty_rate: 19.5
  homeownership_rate: 75.79
  unemployment_rate: 8.37
  median_home_value: 175600
  gini_index: 0.4808
  vacancy_rate: 23.45
  race_white: 17283
  race_black: 221
  race_asian: 250
  race_native: 491
  hispanic: 13288
  bachelors_plus: 9202
districts:
  - to: "us/states/nm/districts/02"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nm/districts/senate/35"
    rel: in-district
    area_weight: 0.6093
  - to: "us/states/nm/districts/senate/28"
    rel: in-district
    area_weight: 0.3905
  - to: "us/states/nm/districts/house/39"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Grant County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 27775 |
| Under 18 | 4974 |
| 18–64 | 14382 |
| 65+ | 8419 |
| Median household income | 44958 |
| Poverty rate | 19.5 |
| Homeownership rate | 75.79 |
| Unemployment rate | 8.37 |
| Median home value | 175600 |
| Gini index | 0.4808 |
| Vacancy rate | 23.45 |
| White | 17283 |
| Black | 221 |
| Asian | 250 |
| Native | 491 |
| Hispanic/Latino | 13288 |
| Bachelor's or higher | 9202 |

## Districts

- [NM-02](/us/states/nm/districts/02.md) — 100% (congressional)
- [NM Senate District 35](/us/states/nm/districts/senate/35.md) — 61% (state senate)
- [NM Senate District 28](/us/states/nm/districts/senate/28.md) — 39% (state senate)
- [NM House District 39](/us/states/nm/districts/house/39.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
