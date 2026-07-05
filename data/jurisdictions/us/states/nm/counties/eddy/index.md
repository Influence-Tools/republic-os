---
type: Jurisdiction
title: "Eddy County, NM"
classification: county
fips: "35015"
state: "NM"
demographics:
  population: 61105
  population_under_18: 15759
  population_18_64: 36312
  population_65_plus: 9034
  median_household_income: 78426
  poverty_rate: 13.84
  homeownership_rate: 73.35
  unemployment_rate: 5.5
  median_home_value: 212600
  gini_index: 0.4532
  vacancy_rate: 11.99
  race_white: 34593
  race_black: 877
  race_asian: 359
  race_native: 986
  hispanic: 31515
  bachelors_plus: 10823
districts:
  - to: "us/states/nm/districts/02"
    rel: in-district
    area_weight: 0.9211
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 0.0787
  - to: "us/states/nm/districts/senate/34"
    rel: in-district
    area_weight: 0.4535
  - to: "us/states/nm/districts/senate/42"
    rel: in-district
    area_weight: 0.305
  - to: "us/states/nm/districts/senate/41"
    rel: in-district
    area_weight: 0.1839
  - to: "us/states/nm/districts/senate/32"
    rel: in-district
    area_weight: 0.0576
  - to: "us/states/nm/districts/house/66"
    rel: in-district
    area_weight: 0.3391
  - to: "us/states/nm/districts/house/54"
    rel: in-district
    area_weight: 0.3308
  - to: "us/states/nm/districts/house/55"
    rel: in-district
    area_weight: 0.3301
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Eddy County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 61105 |
| Under 18 | 15759 |
| 18–64 | 36312 |
| 65+ | 9034 |
| Median household income | 78426 |
| Poverty rate | 13.84 |
| Homeownership rate | 73.35 |
| Unemployment rate | 5.5 |
| Median home value | 212600 |
| Gini index | 0.4532 |
| Vacancy rate | 11.99 |
| White | 34593 |
| Black | 877 |
| Asian | 359 |
| Native | 986 |
| Hispanic/Latino | 31515 |
| Bachelor's or higher | 10823 |

## Districts

- [NM-02](/us/states/nm/districts/02.md) — 92% (congressional)
- [NM-03](/us/states/nm/districts/03.md) — 8% (congressional)
- [NM Senate District 34](/us/states/nm/districts/senate/34.md) — 45% (state senate)
- [NM Senate District 42](/us/states/nm/districts/senate/42.md) — 30% (state senate)
- [NM Senate District 41](/us/states/nm/districts/senate/41.md) — 18% (state senate)
- [NM Senate District 32](/us/states/nm/districts/senate/32.md) — 6% (state senate)
- [NM House District 66](/us/states/nm/districts/house/66.md) — 34% (state house)
- [NM House District 54](/us/states/nm/districts/house/54.md) — 33% (state house)
- [NM House District 55](/us/states/nm/districts/house/55.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
