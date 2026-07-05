---
type: Jurisdiction
title: "Lea County, NM"
classification: county
fips: "35025"
state: "NM"
demographics:
  population: 73733
  population_under_18: 21754
  population_18_64: 43601
  population_65_plus: 8378
  median_household_income: 68015
  poverty_rate: 18.69
  homeownership_rate: 71.18
  unemployment_rate: 6.87
  median_home_value: 184000
  gini_index: 0.4886
  vacancy_rate: 13.14
  race_white: 31609
  race_black: 2525
  race_asian: 788
  race_native: 687
  hispanic: 46266
  bachelors_plus: 10121
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 0.5346
  - to: "us/states/nm/districts/02"
    rel: in-district
    area_weight: 0.4653
  - to: "us/states/nm/districts/senate/41"
    rel: in-district
    area_weight: 0.5444
  - to: "us/states/nm/districts/senate/27"
    rel: in-district
    area_weight: 0.272
  - to: "us/states/nm/districts/senate/42"
    rel: in-district
    area_weight: 0.1835
  - to: "us/states/nm/districts/house/66"
    rel: in-district
    area_weight: 0.4043
  - to: "us/states/nm/districts/house/55"
    rel: in-district
    area_weight: 0.3188
  - to: "us/states/nm/districts/house/61"
    rel: in-district
    area_weight: 0.2255
  - to: "us/states/nm/districts/house/62"
    rel: in-district
    area_weight: 0.0513
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Lea County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 73733 |
| Under 18 | 21754 |
| 18–64 | 43601 |
| 65+ | 8378 |
| Median household income | 68015 |
| Poverty rate | 18.69 |
| Homeownership rate | 71.18 |
| Unemployment rate | 6.87 |
| Median home value | 184000 |
| Gini index | 0.4886 |
| Vacancy rate | 13.14 |
| White | 31609 |
| Black | 2525 |
| Asian | 788 |
| Native | 687 |
| Hispanic/Latino | 46266 |
| Bachelor's or higher | 10121 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 53% (congressional)
- [NM-02](/us/states/nm/districts/02.md) — 47% (congressional)
- [NM Senate District 41](/us/states/nm/districts/senate/41.md) — 54% (state senate)
- [NM Senate District 27](/us/states/nm/districts/senate/27.md) — 27% (state senate)
- [NM Senate District 42](/us/states/nm/districts/senate/42.md) — 18% (state senate)
- [NM House District 66](/us/states/nm/districts/house/66.md) — 40% (state house)
- [NM House District 55](/us/states/nm/districts/house/55.md) — 32% (state house)
- [NM House District 61](/us/states/nm/districts/house/61.md) — 23% (state house)
- [NM House District 62](/us/states/nm/districts/house/62.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
